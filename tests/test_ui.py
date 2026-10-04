"""Test the UI question-visibility logic."""

from __future__ import annotations

from scicookie.ui import check_visibility


def test_check_visibility_unanswered_dependency_is_not_satisfied() -> None:
    """A `depends_on` key not yet in `answers` must not crash.

    `make_questions` calls `check_visibility` once per question, in the order
    questions appear in the profile yaml, filling in `answers` as it goes. A
    `depends_on` referencing a question that hasn't been answered yet (out of
    order, or a typo in the yaml) used to crash with `KeyError` from a plain
    `answers[crit_key]` lookup, instead of simply treating the dependency as
    unsatisfied.
    """
    question = {
        "visible": True,
        "depends_on": [{"not_yet_answered": "yes"}],
    }
    assert check_visibility(question, {}) is False
