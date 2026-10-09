"""Test the UI question-rendering logic."""

from __future__ import annotations

from unittest.mock import patch

from scicookie.ui import make_questions


def test_make_questions_missing_help_key_does_not_crash() -> None:
    """A question without a `help` key must not crash `make_questions`.

    `_create_question` already treats `help` as optional (`question.get(
    "help")`, left unused behind a `todo` comment), but `make_questions`
    itself printed it unconditionally with `question["help"]` -- a plain
    user-defined profile question that omits `help` (unlike every question
    in this project's own `base.yaml`/`osl.yaml`, which all happen to set
    it) used to crash with `KeyError` instead of simply showing no help
    text, the same way a missing `default_answer`/`message` already falls
    back to an empty value a few lines above.
    """
    questions = {
        "project_name": {
            "type": "text",
            "visible": True,
            "message": "What is the project name?",
            "default": "my-project",
        },
    }

    with patch(
        "scicookie.ui.inquirer.prompt",
        return_value={"project_name": "my-project"},
    ):
        answers = make_questions(questions)

    assert answers == {"project_name": "my-project"}
