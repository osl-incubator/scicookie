"""Cookiecutter bake test."""

from pathlib import Path

import pytest


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


@pytest.mark.parametrize(
    "build_system,expected_lock,unexpected_lock",
    [
        ("uv", "uv.lock", "poetry.lock"),
        ("poetry", "poetry.lock", "uv.lock"),
        ("pdm", "pdm.lock", "uv.lock"),
        ("maturin", "Cargo.lock", "uv.lock"),
    ],
)
def test_gitignore_lockfile_for_build_system(
    cookies, context, build_system, expected_lock, unexpected_lock
):
    """Test lockfile configuration in .gitignore for build systems."""
    result = cookies.bake(
        extra_context={**context, "build_system": build_system}
    )
    assert result.exit_code == 0
    assert result.exception is None
    gitignore_path = Path(result.project_path) / ".gitignore"
    assert gitignore_path.is_file()
    content = gitignore_path.read_text()
    assert expected_lock in content
    assert unexpected_lock not in content
