"""Test the SciCookie CLI."""

from __future__ import annotations

import re
import shutil
import tempfile

from pathlib import Path
from typing import Any

import pexpect
import pytest
import yaml


@pytest.fixture
def setup_test_main_yaml() -> None:
    """Copy the test YAML profile for testing and remove it after the test."""
    test_dir = Path(__file__).parent
    src_dir = test_dir.parent / "src" / "scicookie"

    profile_src_path = test_dir / "profiles" / "test-main.yaml"
    profile_dest_path = src_dir / "profiles" / "test-main.yaml"
    shutil.copy(profile_src_path, profile_dest_path)

    # Create a temporary directory using the tempfile module
    with tempfile.TemporaryDirectory() as tmp_dir:
        shutil.copy(profile_src_path, profile_dest_path)
        # Provide the temporary directory path to the test
        yield {"tmp_dir": tmp_dir}
        # The temporary directory is automatically cleaned up here

    # Cleanup after test
    profile_dest_path.unlink()


@pytest.fixture
def all_questions_main_yaml() -> dict[str, Any]:
    """Load all questions from the base.yaml configuration for testing."""
    test_dir = Path(__file__).parent
    profile_path = test_dir / "profiles" / "test-main.yaml"
    with open(profile_path) as f:
        return yaml.safe_load(f)


def test_main(
    setup_test_main_yaml: dict[str, str],
    all_questions_main_yaml: dict[str, Any],
) -> None:
    """Test with test-main.yaml."""
    all_questions = all_questions_main_yaml
    tmp_dir = setup_test_main_yaml.get("tmp_dir", "/tmp")

    child = pexpect.spawn(
        "scicookie --profile test-main",
        cwd=tmp_dir,
        encoding="utf-8",
        timeout=10,
    )

    for key, value in all_questions.items():
        prompt = value.get("message")
        if prompt:
            # Escape special characters and allow any whitespace after
            regex_prompt = re.escape(prompt) + r"\s*"
            # Use regex for matching the prompt
            child.expect(regex_prompt, timeout=10)
            response = value.get("default", "")
            child.sendline(response)

    child.expect(pexpect.EOF)
    output = child.before
    assert "Traceback" not in output, output
