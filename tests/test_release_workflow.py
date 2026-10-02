"""Tests for the release workflow shipped in the generated project."""

from pathlib import Path

import pytest
import yaml


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
        "use_github_actions": "yes",
    }


def read_publish_dir(project_path):
    """Return the publish_dir given to the GitHub Pages action."""
    workflow_path = (
        Path(project_path) / ".github" / "workflows" / "release.yaml"
    )
    assert workflow_path.is_file()
    workflow = yaml.safe_load(workflow_path.read_text())
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "actions-gh-pages" in str(step.get("uses", "")):
                return step["with"]["publish_dir"]
    return None


@pytest.mark.parametrize(
    ("documentation_engine", "expected_publish_dir"),
    [
        ("mkdocs", "build/"),
        ("sphinx(rst)", "docs/_build/html/"),
        ("sphinx(myst)", "docs/_build/html/"),
        ("jupyter-book", "./docs/_build/html"),
    ],
)
def test_publish_dir_matches_documentation_engine(
    cookies, context, documentation_engine, expected_publish_dir
):
    """Publish the directory the selected documentation engine builds into."""
    result = cookies.bake(
        extra_context={
            **context,
            "documentation_engine": documentation_engine,
        }
    )
    assert result.exit_code == 0
    assert result.exception is None
    assert read_publish_dir(result.project_path) == expected_publish_dir


@pytest.mark.xfail(
    strict=True,
    reason=(
        "quarto has no publish_dir branch, and docs-quarto/_quarto.yml does "
        "not declare an output-dir, so the right value is not known yet"
    ),
)
def test_publish_dir_is_set_for_quarto(cookies, context):
    """Publish a real directory for quarto as well."""
    result = cookies.bake(
        extra_context={**context, "documentation_engine": "quarto"}
    )
    assert result.exit_code == 0

    publish_dir = read_publish_dir(result.project_path)
    # publish_dir uses a YAML folded scalar, where "#" is content and not a
    # comment, so the placeholder would be passed on as a real path
    assert not publish_dir.lstrip().startswith("#")
