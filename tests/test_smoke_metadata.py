"""Validate metadata used by the generated-project smoke tests."""

import sys

import pytest

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


@pytest.mark.parametrize("project_layout", ["src", "flat"])
@pytest.mark.parametrize(
    "build_system", ["flit", "mesonpy", "pdm", "hatch", "maturin"]
)
def test_build_metadata(cookies, project_layout, build_system):
    """Build backends must receive valid PEP 621 metadata."""
    result = cookies.bake(
        extra_context={
            "build_system": build_system,
            "project_layout": project_layout,
            "package_slug": "different_module",
        }
    )
    assert result.exit_code == 0
    metadata = tomllib.loads(
        (result.project_path / "pyproject.toml").read_text()
    )
    assert "packages" not in metadata["project"]
    if build_system == "flit":
        assert metadata["tool"]["flit"]["module"]["name"] == "different_module"


@pytest.mark.parametrize("build_system", ["poetry", "uv"])
@pytest.mark.parametrize("engine", ["sphinx(rst)", "jupyter-book", "quarto"])
def test_documentation_dependencies(cookies, build_system, engine):
    """Documentation projects must declare compatible build dependencies."""
    result = cookies.bake(
        extra_context={
            "build_system": build_system,
            "documentation_engine": engine,
            "use_makim": "yes",
        }
    )
    assert result.exit_code == 0
    metadata = tomllib.loads(
        (result.project_path / "pyproject.toml").read_text()
    )
    if build_system == "poetry":
        dependencies = metadata["tool"]["poetry"]["group"]["dev"][
            "dependencies"
        ]
        assert "click" in dependencies
        if engine == "quarto":
            assert dependencies["griffe"] == "<2"
        elif engine == "jupyter-book":
            assert dependencies["jupyter-book"] == ">=0.15.1,<2"
    else:
        dependencies = metadata["project"]["optional-dependencies"]["dev"]
        assert "click >= 8" in dependencies
        if engine == "quarto":
            assert "griffe < 2" in dependencies
        elif engine == "jupyter-book":
            assert "jupyter-book >= 0.15.1,<2" in dependencies
