"""Cookiecutter bake test."""

import subprocess

from pathlib import Path

import pytest

from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

TEMPLATE_PATH = Path(__file__).parent.parent / "src" / "scicookie"


def git(repo_path: Path, *args: str) -> str:
    """Run a git command inside the given repository."""
    result = subprocess.run(
        ["git", "-C", str(repo_path), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip()


@pytest.fixture
def context():
    """Generate initial context for tests."""
    return {
        "author_full_name": "Sir Example",
        "author_email": "example@ex.ex",
        "project_name": "Example",
        "project_slug": "example",
        "project_short_description": "This is an example",
        "project_url": "example.com",
        "project_version": "0.1.0",
        "documentation_engine": "sphinx(rst)",
    }


def test_bake_project(cookies):
    """Run simple test for cookiecutter."""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "osl-python-package"
    assert result.project_path.is_dir()


def test_project_generation_with_example_context(cookies, context):
    """Run tests with input from the fixture context."""
    result = cookies.bake(extra_context={**context})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()


def test_if_documentation_engine_is_sphinx_with_example_context(
    cookies, context
):
    """Test if the sphinx config file was correctly stored."""
    result = cookies.bake(extra_context={**context})
    assert result.exit_code == 0
    assert result.exception is None
    SPHINX_CONF_PATH = Path(result.project_path) / "docs" / "conf.py"
    sphinx_file_exists = Path.is_file(SPHINX_CONF_PATH)
    assert sphinx_file_exists


def test_project_name_with_example_context(cookies, context):
    """Test context title (project name) is used correctly."""
    result = cookies.bake(extra_context={**context})
    assert result.exit_code == 0
    assert result.exception is None
    README_FILE = Path(result.project_path) / "README.md"
    with open(README_FILE) as f:
        title = f.readline().rstrip()
        assert title == "# Example"


def test_git_main_branch_with_slash(cookies):
    """Test if a main branch name with a slash is used as given."""
    result = cookies.bake(extra_context={"git_main_branch": "release/1.0"})
    assert result.exit_code == 0
    assert result.exception is None
    assert git(result.project_path, "branch", "--show-current") == (
        "release/1.0"
    )
    assert git(result.project_path, "log", "--format=%s") == (
        "Initial commit from SciCookie"
    )


def test_failed_git_init_keeps_parent_repository_untouched(tmp_path):
    """Test if a failed git init does not change an outer repository."""
    git(tmp_path, "init", "-b", "main")
    (tmp_path / "README.md").write_text("parent")
    git(tmp_path, "add", ".")
    git(
        tmp_path,
        "-c",
        "user.name=Parent",
        "-c",
        "user.email=parent@ex.ex",
        "commit",
        "-m",
        "Parent commit",
    )

    with pytest.raises(FailedHookException):
        cookiecutter(
            str(TEMPLATE_PATH),
            no_input=True,
            output_dir=str(tmp_path),
            extra_context={"git_main_branch": "invalid..branch"},
        )

    assert git(tmp_path, "log", "--format=%s") == "Parent commit"
    assert git(tmp_path, "config", "--local", "user.name") == ""
