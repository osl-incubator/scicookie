"""Check generated metadata for the configurations used by smoke tests."""

import pytest


@pytest.mark.parametrize("build_system", ["poetry", "flit"])
@pytest.mark.parametrize("documentation_engine", ["sphinx(rst)", "quarto"])
def test_smoke_dependencies(cookies, build_system, documentation_engine):
    """Keep generated metadata valid and documentation tools compatible."""
    result = cookies.bake(
        extra_context={
            "build_system": build_system,
            "documentation_engine": documentation_engine,
            "use_makim": "yes",
            "use_prettier": "yes",
        }
    )
    assert result.exit_code == 0
    assert result.exception is None
    tomllib = pytest.importorskip("tomllib")
    metadata = tomllib.loads(
        (result.project_path / "pyproject.toml").read_text()
    )
    assert "packages" not in metadata["project"]
    if build_system == "poetry":
        dependencies = metadata["tool"]["poetry"]["group"]["dev"][
            "dependencies"
        ]
        assert dependencies["click"] == ">=8"
        if documentation_engine == "quarto":
            assert dependencies["griffe"] == "<2"
        else:
            assert "griffe" not in dependencies
    else:
        dependencies = metadata["project"]["optional-dependencies"]["dev"]
        assert "click >= 8" in dependencies
        if documentation_engine == "quarto":
            assert "griffe < 2" in dependencies
        else:
            assert "griffe < 2" not in dependencies
