"""Cookiecutter bake test."""

import subprocess

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


def test_prepare_git_with_slash_in_main_branch(cookies, context):
    """Check a main branch name with a slash survives prepare_git.

    `git_main_branch` is a branch name, not a URL, but it used to be run
    through the same URL-to-SSH helper as `git_https_origin`/
    `git_https_upstream`. That helper turns the first "/" into a ":", and
    git refuses to create a branch whose name contains a colon, so any
    main-branch name with a slash in it (e.g. "release/1.0") broke
    `git init -b <branch>` outright.
    """
    result = cookies.bake(
        extra_context={**context, "git_main_branch": "release/1.0"}
    )
    assert result.exit_code == 0
    assert result.exception is None

    branch = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=result.project_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    assert branch == "release/1.0"
