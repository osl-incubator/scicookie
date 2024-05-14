"""Module with CLI functions."""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys

from pathlib import Path
from typing import Union

from cookiecutter.main import cookiecutter

from scicookie.logs import SciCookieErrorType, SciCookieLogs
from scicookie.profile import Profile
from scicookie.ui import make_questions

PACKAGE_PATH = Path(__file__).parent
COOKIECUTTER_FILE_PATH = PACKAGE_PATH / "cookiecutter.json"


class CustomHelpFormatter(argparse.RawTextHelpFormatter):
    """Formatter for generating usage messages and argument help strings.

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """

    def __init__(
        self,
        prog,
        indent_increment=2,
        max_help_position=4,
        width=None,
        **kwargs,
    ):
        """Define the parameters for the argparse help text."""
        super().__init__(
            prog,
            indent_increment=indent_increment,
            max_help_position=max_help_position,
            width=width,
            **kwargs,
        )


def _get_cookiecutter_default_answer(
    answer_definition: Union[str, list],
) -> str:
    if not isinstance(answer_definition, (str, list)):
        SciCookieLogs.raise_error(
            "Invalid cookiecutter configuration.",
            SciCookieErrorType.SCICOOKIE_INVALID_CONFIGURATION,
        )

    if isinstance(answer_definition, str):
        return answer_definition

    return answer_definition[0]


def call_cookiecutter(profile: Profile, answers: dict) -> None:
    """Call cookiecutter/cookiecutter with the parameters from the TUI."""
    answers_profile = {}
    questions = profile.config

    with open(COOKIECUTTER_FILE_PATH) as f:
        cookiecutter_config = json.load(f)

    # fill the answers with default value
    for question_id, question in questions.items():
        if question.get("control_flow", False):
            # "control_flow" is not defined in cookiecutter config
            continue

        if not question.get("visible", False):
            # get the default for non visible questions
            answers_profile[question_id] = question.get("default")
            continue

        if question.get("type") == "multiple-choices":
            for choice in question.get("choices", {}):
                choice_id = f"use_{choice.replace('-', '_')}"
                answers_profile[choice_id] = "no"
            continue

        answers_profile[question_id] = question.get(
            "default"
        ) or _get_cookiecutter_default_answer(cookiecutter_config[question_id])

    for question_id, answer in answers.items():
        if answer in [None, ""] or questions[question_id].get("control_flow"):
            continue

        if questions[question_id].get("type") != "multiple-choices":
            answers_profile[question_id] = answer
            continue

        for choice in answer:
            choice_id = f"use_{choice.replace('-', '_')}"
            answers_profile[choice_id] = "yes"

    env_path_sep = ";" if platform.system() == "Windows" else ":"
    pipx_path: list[str] = list(filter(lambda v: ".local/pipx" in v, sys.path))
    new_path: list[str] = [*pipx_path, os.getenv("PATH", "")]
    os.environ["PATH"] = env_path_sep.join(new_path)

    cookiecutter(
        str(PACKAGE_PATH), no_input=True, extra_context=answers_profile
    )


def call_app(profile_name: str) -> None:
    """Call the scicookie app."""
    profile = Profile(profile_name)

    answers = make_questions(profile.config)

    if not answers:
        return

    call_cookiecutter(profile, answers)


def app() -> None:
    """Run SciCookie."""
    # note: this parameter should be provided by a CLI argument

    parser = argparse.ArgumentParser(
        prog="SciCookie",
        description=(
            "SciCookie is a template developed by Open Science Labs that "
            "creates projects through different options of profile. "
            "It serves as a boilerplate which can be used by beginners as "
            "well as full fledged developers to simplify the project creation "
            "process and save considerable amount of time. It creates  "
            "projects with an initial layout that includes recommended  "
            "tools, workflows, and project structure."
        ),
        epilog=(
            "If you have any problem, open an issue at: "
            "https://github.com/osl-incubator/scicookie"
        ),
        add_help=True,
        formatter_class=CustomHelpFormatter,
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="base",
        help="Select the profile to be used",
    )

    args = parser.parse_args()
    call_app(args.profile)
