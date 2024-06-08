"""Test the SciCookie CLI."""

from __future__ import annotations

import re
import shutil
import sys
import tempfile

from pathlib import Path
from typing import Any

import pexpect
import pytest
import yaml

from scicookie.ui import check_visibility


def get_all_questions(profile_file_name: str) -> dict[str, Any]:
    """Load all questions from the given configuration file for testing."""
    test_dir = Path(__file__).parent
    profile_path = test_dir / "profiles" / profile_file_name
    with open(profile_path) as f:
        return yaml.safe_load(f)


@pytest.fixture
def tmp_dir() -> str:
    """Create a temporary folder."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield tmp_dir


@pytest.mark.skipif(not sys.platform.startswith("linux"), reason="Linux only")
class BaseCLITestProfile:
    """Tests for test-main.yaml."""

    profile_path: str = ""
    profile_filename: str = ""

    @classmethod
    def setup_class(cls):
        """Configure initial settings for the class."""
        test_dir = Path(__file__).parent
        src_dir = test_dir.parent / "src" / "scicookie"

        profile_src_path = test_dir / "profiles" / cls.profile_filename
        cls.profile_path = src_dir / "profiles" / cls.profile_filename

        shutil.copy(profile_src_path, cls.profile_path)

    @classmethod
    def teardown_class(cls):
        """Cleanup after test."""
        cls.profile_path.unlink()


@pytest.mark.skipif(not sys.platform.startswith("linux"), reason="Linux only")
class TestMain(BaseCLITestProfile):
    """Tests for test-main.yaml."""

    profile_filename: str = "test-main.yaml"

    def test_cli(self, tmp_dir: str) -> None:
        """Test with test-main.yaml."""
        all_questions = get_all_questions(self.profile_filename)

        child = pexpect.spawn(
            "scicookie --profile test-main",
            cwd=tmp_dir,
            encoding="utf-8",
            timeout=10,
        )

        answers = {}

        for key, value in all_questions.items():
            if not check_dependencies_satisfied(value, answers):
                continue

            prompt = value.get("message")
            if prompt:
                # Escape special characters and allow any whitespace after
                regex_prompt = re.escape(prompt) + r"\s*"
                # Use regex for matching the prompt
                child.expect(regex_prompt, timeout=10)
                response = value.get("default", "")
                answers[key] = response
                child.sendline(response)

        child.expect(pexpect.EOF)
        output = child.before
        assert "Traceback" not in output, output


@pytest.mark.skipif(not sys.platform.startswith("linux"), reason="Linux only")
class TestDependsOn(BaseCLITestProfile):
    """Tests for test-main.yaml."""

    profile_filename: str = "test-depends-on.yaml"

    def test_cli(self, tmp_dir: str) -> None:
        """Test with test-main.yaml."""
        all_questions = get_all_questions(self.profile_filename)

        child = pexpect.spawn(
            "scicookie --profile test-depends-on",
            cwd=tmp_dir,
            encoding="utf-8",
            timeout=10,
        )

        answers = {}

        for key, value in all_questions.items():
            if not check_visibility(value, answers):
                continue

            prompt = value.get("message")

            if not prompt:
                continue

            # Escape special characters and allow any whitespace after
            regex_prompt = re.escape(prompt) + r"\s*"
            # Use regex for matching the prompt
            child.expect(regex_prompt, timeout=10)
            response = value.get("default", "")
            answers[key] = response
            child.sendline(response)

        child.expect(pexpect.EOF)
        output = child.before
        assert "Traceback" not in output, output
