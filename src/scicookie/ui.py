"""Define functions for the interface with the user."""
from __future__ import annotations

import os

from typing import Any, Optional, Type

import inquirer

from colorama import Fore, Style, init
from jinja2 import Template

from scicookie.logs import SciCookieErrorType, SciCookieLogs

# Initialize Colorama
init()


def _create_question(
    question_id: str, question: dict
) -> Optional[inquirer.questions.Question]:
    # validation
    if not question.get("visible", False):
        return None

    # config required
    question_type = question.get("type", "")
    # todo: implement help text int he prompt
    # question_help = question.get("help")
    # todo: implement depends on workflow, it needs refactoring the code
    #       because it needs access to the answer
    # question_depends_on = question.get("depends_on")
    # it should allow multiple conditionals

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


def check_dependencies_satisfied(
    question: dict[str, Any], answers: dict[str, str]
) -> bool:
    """
    Check if dependencies are satisfied.

    Note: Not implemented yet.
    """
    return True


def make_questions(questions: dict[str, Any]) -> dict[str, str]:
    """Generate all the visible questions."""
    answers: dict[str, str] = {}

    # Get the size of the terminal window
    columns, _ = os.get_terminal_size()

    # Print a line
    print("-" * columns)
    print(
        Fore.YELLOW
        + "NOTE: "
        + Fore.RESET
        + "For questions with single or multiple choices, use the ARROW "
        + "keys to navigate through the options. Use the SPACE BAR to "
        + "select or deselect an option. Confirm your selection with "
        + "the ENTER key."
    )
    print("." * columns)

    for question_id, question in questions.items():
        question_obj = _create_question(question_id, question)

        default_answer = question.get("default", "")
        default_answer = Template(default_answer).render(answers)

        # note: if question_object is None, that means that the question is
        #       not visible
        if not (
            check_dependencies_satisfied(question, answers) and question_obj
        ):
            answers[question_id] = default_answer
            continue

        message = question.get("message", "")
        print(
            Style.BRIGHT
            + f"{message} ("
            + Fore.YELLOW
            + f"default: {default_answer}"
            + Fore.RESET
            + Style.BRIGHT
            + "):"
            + Fore.RESET
        )
        print(Fore.BLUE + ">> HELP: " + question["help"] + Fore.RESET)
        answer = inquirer.prompt([question_obj])

        # note: if answer is none, it means that the user cancelled
        #       the process.
        if answer is None:
            return {}
        answers[question_id] = answer.get(question_id, "") or default_answer
        print("." * columns)
    return answers
