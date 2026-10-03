"""Test generation of projects that use Zensical documentation."""

import json
import sys

from pathlib import Path

import pytest
import yaml

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


@pytest.mark.parametrize("build_system", ["poetry", "uv"])
@pytest.mark.parametrize("project_layout", ["src", "flat"])
def test_zensical_project(cookies, build_system, project_layout):
    """Generate usable documentation without MkDocs-specific tooling."""
    result = cookies.bake(
        extra_context={
            "documentation_engine": "zensical",
            "build_system": build_system,
            "project_layout": project_layout,
            "use_make": "yes",
            "use_makim": "yes",
            "use_github_actions": "yes",
        }
    )
    assert result.exit_code == 0
    assert result.exception is None
    project = result.project_path
    assert (project / "zensical.toml").is_file()
    assert (project / "docs/index.md").is_file()
    assert not (project / "docs-zensical").exists()
    assert not (project / "mkdocs.yaml").exists()
    assert not (project / "scripts/gen_ref_nav.py").exists()
    metadata = (project / "pyproject.toml").read_text()
    tomllib.loads(metadata)
    assert "zensical" in metadata
    assert "mkdocs" not in metadata
    makefile = (project / "Makefile").read_text()
    assert "zensical build" in makefile
    assert "zensical serve" in makefile
    tasks = yaml.safe_load((project / ".makim.yaml").read_text())
    assert tasks["groups"]["docs"]["tasks"]["build"]["run"].strip() == (
        "zensical build"
    )
    assert tasks["groups"]["docs"]["tasks"]["preview"]["run"].strip() == (
        "zensical serve"
    )
    workflow = yaml.safe_load(
        (project / ".github/workflows/release.yaml").read_text()
    )
    publish_steps = [
        step
        for job in workflow["jobs"].values()
        for step in job.get("steps", [])
        if step.get("uses", "").startswith("peaceiris/actions-gh-pages")
    ]
    assert publish_steps[0]["with"]["publish_dir"] == "build/"


def test_zensical_available_in_profiles():
    """Offer the engine in interactive and direct Cookiecutter generation."""
    template = Path(__file__).parent.parent / "src/scicookie"
    context = json.loads((template / "cookiecutter.json").read_text())
    profile = yaml.safe_load((template / "profiles/base.yaml").read_text())
    assert "zensical" in context["documentation_engine"]
    assert "zensical" in profile["documentation_engine"]["choices"]
