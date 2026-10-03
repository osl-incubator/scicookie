"""Test profile defaults without an interactive terminal."""

from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from scicookie import cli, ui


@pytest.mark.parametrize("visible", [True, False])
@pytest.mark.parametrize("default", [["ruff", "mypy"], [], "ruff"])
def test_question_defaults(monkeypatch, visible, default):
    """Preserve list and string defaults for unanswered questions."""
    questions = {
        "tools": {
            "type": "multiple-choices",
            "choices": ["ruff", "mypy"],
            "default": default,
            "visible": visible,
            "help": "Select tools",
        }
    }
    monkeypatch.setattr(ui.inquirer, "prompt", lambda _: {"tools": []})
    assert ui.make_questions(questions) == {"tools": default}


def test_render_list_defaults(monkeypatch):
    """Render each default using answers to earlier questions."""
    questions = {
        "tool": {"type": "text", "default": "ruff", "visible": False},
        "tools": {
            "type": "multiple-choices",
            "default": [" ${{ tool }} ", "mypy"],
            "visible": False,
        },
    }
    assert ui.make_questions(questions)["tools"] == ["ruff", "mypy"]


@pytest.mark.parametrize("visible", [True, False])
@pytest.mark.parametrize(
    "answers, expected",
    [
        ({}, ["yes", "yes"]),
        ({"tools": ["mypy"]}, ["no", "yes"]),
        ({"tools": []}, ["no", "no"]),
    ],
)
def test_generation_defaults(monkeypatch, visible, answers, expected):
    """Convert defaults to flags and let explicit answers replace them."""
    profile = SimpleNamespace(
        config={
            "tools": {
                "type": "multiple-choices",
                "choices": ["ruff", "mypy"],
                "default": ["ruff", "mypy"],
                "visible": visible,
            }
        }
    )
    generate = Mock()
    monkeypatch.setattr(cli, "cookiecutter", generate)
    cli.call_cookiecutter(profile, answers)
    context = generate.call_args.kwargs["extra_context"]
    assert context == dict(zip(["use_ruff", "use_mypy"], expected))
