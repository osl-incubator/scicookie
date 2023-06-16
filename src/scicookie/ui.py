"""Define functions for the interface with the user."""
from typing import Optional, Type, Dict
import inquirer
from scicookie.logs import SciCookieErrorType, SciCookieLogs


def _create_question(
    question_id: str, question: dict
) -> Optional[inquirer.questions.Question]:
    # validation
    if not question.get("enabled", False):
        return None

    # config required
    default_answer = question.get("default", "")
    question_message = question.get("message", "")
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

    content = {
        "message": (
            question_message
            if not default_answer
            else f"{question_message} (default: {default_answer})"
        )
    }

    if question.get("choices"):
        content["choices"] = question.get("choices")

    fn_questions: Dict[str, Type[inquirer.questions.Question]] = {
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
    questions_ui = []

    for question_id, question in questions.items():
        question_obj = _create_question(question_id, question)
        if question_obj:
            questions_ui.append(question_obj)

    return inquirer.prompt(questions_ui)
