"""Define functions for the interface with the user."""

from __future__ import annotations

import os
import re

from typing import Any, Optional, Type, Union, cast

import inquirer

from colorama import Fore, Style, init
from jinja2 import Environment

from scicookie.logs import SciCookieErrorType, SciCookieLogs

ENV = Environment(
    autoescape=False,
    variable_start_string="${{",
    variable_end_string="}}",
)


# Initialize Colorama
init()


def _create_question(
    question_id: str, question: dict
) -> Optional[inquirer.questions.Question]:
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


def check_visibility(
    question: dict[str, Any], answers: dict[str, str]
) -> bool:
    """Check if dependencies are satisfied."""
    # validation
    is_visible: Union[str, bool] = question.get("visible", False)

    if isinstance(is_visible, str):
        is_visible = (
            ENV.from_string(is_visible).render(answers).strip() == "True"
        )

    if not cast(bool, is_visible):
        return False

    if "depends_on" not in question:
        return True

    depends_satisfied = True
    depends_on_attr = question.get("depends_on", [])

    if not isinstance(depends_on_attr, list):
        raise Exception("`depends_on` attribute is a list of dictionaries.")

    for criteria_or in depends_on_attr:
        if not isinstance(criteria_or, dict):
            raise Exception(
                "`depends_on` attribute is a list of dictionaries."
            )

        tmp_satisfied = False

        for crit_key, crit_value in criteria_or.items():
            if answers[crit_key] == crit_value:
                tmp_satisfied = True

        depends_satisfied = depends_satisfied and tmp_satisfied

    return depends_satisfied


def sanitize_package_slug(package_slug: str) -> str:
    """Filter to sanitize the package slug."""
    return re.sub(
        r"^\s+|\s+$", "", re.sub(r"[^a-zA-Z0-9_]+", "", package_slug)
    )


def make_questions(questions: dict[str, Any]) -> dict[str, str]:
    """Generate all the visible questions."""
    answers: dict[str, str] = {}

    # Get the size of the terminal window
    try:
        columns, _ = os.get_terminal_size()
    except OSError:
        columns = 80

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

    # Create a Jinja2 environment and add the custom filter
    ENV.filters["sanitize_package_slug"] = sanitize_package_slug

    for question_id, question in questions.items():
        question_obj = _create_question(question_id, question)

        default_answer = question.get("default", "")
        default_answer = (
            ENV.from_string(default_answer).render(answers).strip()
        )

        # note: if question_object is None, that means that the question is
        #       not visible
        if not (check_visibility(question, answers) and question_obj):
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
