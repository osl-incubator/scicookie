"""Module with CLI functions."""
import json
import os
import sys
from pathlib import Path
from typing import Union

import sh

from scicookie.logs import SciCookieErrorType, SciCookieLogs
from scicookie.profile import Profile
from scicookie.ui import make_questions

PACKAGE_PATH = Path(__file__).parent
COOKIECUTTER_FILE_PATH = PACKAGE_PATH / "cookiecutter.json"


def _get_cookiecutter_default_answer(
    answer_definition: Union[str, list]
) -> str:
    if not isinstance(answer_definition, (str, list)):
        SciCookieLogs.raise_error(
            "Invalid cookiecutter configuration.",
            SciCookieErrorType.SCICOOKIE_INVALID_CONFIGURATION,
        )

    if isinstance(answer_definition, str):
        return answer_definition

    return answer_definition[0]


def call_cookiecutter(profile: Profile, answers: dict):
    """Call cookiecutter/cookieninja with the parameters from the TUI."""
    answers_profile = {}
    cookie_args = []
    questions = profile.config

    with open(COOKIECUTTER_FILE_PATH) as f:
        cookiecutter_config = json.load(f)

    # fill the answers with default value
    for question_id, question in questions.items():
        if not question.get("enabled", False) or question.get("control_flow"):
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

    for question_id, answer in answers_profile.items():
        cookie_args.append(f"{question_id}={answer}")

    sh_extras = {
        "_in": sys.stdin,
        "_out": sys.stdout,
        "_err": sys.stderr,
        "_no_err": True,
        "_env": os.environ,
        "_bg": True,
        "_bg_exc": False,
    }

    p = sh.cookieninja("--no-input", PACKAGE_PATH, *cookie_args, **sh_extras)

    try:
        p.wait()
    except sh.ErrorReturnCode as e:
        SciCookieLogs.raise_error(
            str(e), SciCookieErrorType.SH_ERROR_RETURN_CODE
        )
    except KeyboardInterrupt:
        pid = p.pid
        p.kill()
        SciCookieLogs.raise_error(
            f"Process {pid} killed.", SciCookieErrorType.SH_KEYBOARD_INTERRUPT
        )


def app():
    """Run SciCookie."""
    # note: this parameter should be provided by a CLI argument
    profile = Profile("osl")

    answers = make_questions(profile.config)

    if not answers:
        return

    call_cookiecutter(profile, answers)
