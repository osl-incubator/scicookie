"""Cookiecutter bake test."""

from pathlib import Path

import pytest

TEMPLATE_PATH = str(
    Path(__file__).resolve().parent.parent / "src" / "scicookie"
)


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
    result = cookies.bake(template=TEMPLATE_PATH)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "osl-python-package"
    assert result.project_path.is_dir()


def test_project_generation_with_example_context(cookies, context):
    """Run tests with input from the fixture context."""
    result = cookies.bake(template=TEMPLATE_PATH, extra_context={**context})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()


def test_if_documentation_engine_is_sphinx_with_example_context(
    cookies, context
):
    """Test if the sphinx config file was correctly stored."""
    result = cookies.bake(template=TEMPLATE_PATH, extra_context={**context})
    assert result.exit_code == 0
    assert result.exception is None
    sphinx_conf_path = Path(result.project_path) / "docs" / "conf.py"
    assert sphinx_conf_path.is_file()


def test_project_name_with_example_context(cookies, context):
    """Test context title (project name) is used correctly."""
    result = cookies.bake(template=TEMPLATE_PATH, extra_context={**context})
    assert result.exit_code == 0
    assert result.exception is None
    readme_file = Path(result.project_path) / "README.md"
    with open(readme_file) as f:
        title = f.readline().rstrip()
        assert title == "# Example"
