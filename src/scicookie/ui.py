"""Define functions for the interface with the user."""
from __future__ import annotations

from typing import Optional, Type

import inquirer
from jinja2 import Template

from scicookie.logs import SciCookieErrorType, SciCookieLogs


def _create_question(
    question_id: str, question: dict
) -> Optional[inquirer.questions.Question]:
    # validation
    if not question.get("enabled", False):
        return None

    # config required
    question_type = question.get("type", "")
    # todo: implement help text int he prompt
    # question_help = question.get("help")
    # todo: implement depends on workflow, it needs refactoring the code
    #       because it needs access to the answer
    # question_depends_on = question.get("depends_on")

    question_types_available = [
        "text",
        "single-choice",
        "multiple-choices",
        "confirm",
    ]

    if question_type not in question_types_available:
        SciCookieLogs.raise_error(
            f"The question type ({question_type}) is not available ("
            f"{question_types_available}).",
            SciCookieErrorType.SCICOOKIE_INVALID_CONFIGURATION,
        )

    content = {"message": ""}

    if question.get("choices"):
        content["choices"] = question.get("choices", [])

    fn_questions: dict[str, Type[inquirer.questions.Question]] = {
        "text": inquirer.Text,
        "single-choice": inquirer.List,
        "multiple-choices": inquirer.Checkbox,
        "confirm": inquirer.Confirm,
    }

    return fn_questions[question_type](
        question_id,
        **content,
    )


def make_questions(questions: dict):
    """Generate all the enabled questions."""
    answers: dict[str, str] = {}

    for question_id, question in questions.items():
        question_obj = _create_question(question_id, question)
        # note: if question_object is None, that means that the question is
        #       not enabled
        if question_obj:
            default_answer = question.get("default", "")
            default_answer = Template(default_answer).render(answers)
            message = question.get("message", "")
            print(f"{message} (default: {default_answer}):")
            print(">> HELP:", question["help"])
            answer = inquirer.prompt([question_obj])

            # note: if answer is none, it means that the user cancelled
            #       the process.
            if answer is None:
                return {}
            answers[question_id] = (
                answer.get(question_id, "") or default_answer
            )
    return answers
