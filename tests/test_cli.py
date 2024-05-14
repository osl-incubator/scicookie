"""Test the SciCookie CLI."""

from __future__ import annotations

import pytest
import re
import shutil

from io import StringIO
from pathlib import Path
from typing import Any

import pexpect
import yaml

from scicookie.cli import call_app


@pytest.fixture
def setup_test_main_yaml() -> None:
    """Copy the test YAML profile for testing and remove it after the test."""
    test_dir = Path(__file__).parent
    src_dir = test_dir.parent / "src" / "scicookie"

    profile_src_path = test_dir / "profiles" / "test-main.yaml"
    profile_dest_path = src_dir / "profiles" / "test-main.yaml"
    shutil.copy(profile_src_path, profile_dest_path)
    yield
    # Cleanup after test
    profile_dest_path.unlink()


@pytest.fixture
def all_questions() -> dict[str, Any]:
    """Load all questions from the base.yaml configuration for testing."""
    project_dir = Path(__file__).parent.parent
    profile_dir = project_dir / "src" / "scicookie" / "profiles"
    with open(profile_dir / "base.yaml") as f:
        return yaml.safe_load(f)


def test_main(setup_test_main_yaml: None, all_questions: dict[str, Any]):
    child = pexpect.spawn(
        "scicookie --profile test-main", encoding="utf-8", timeout=10
    )

    for key, value in all_questions.items():
        prompt = value.get("message")
        if prompt:
            # Escape special characters and allow any whitespace after
            regex_prompt = re.escape(prompt) + r"\s*"
            # Use regex for matching the prompt
            child.expect(regex_prompt, timeout=10)
            default = value.get("default")
            response = default if default else "Test Input"
            child.sendline(response)

    child.expect(pexpect.EOF)
    output = child.before
    assert "Traceback" not in output, f"Failure found: {output}"
