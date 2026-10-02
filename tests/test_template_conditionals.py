"""Check template conditionals that branch on a choice variable.

The bug this PR fixes was a conditional comparing one cookiecutter variable
against a value belonging to a different variable. Such a branch can never be
taken, so the user silently ends up in the fallback branch with no error.

This test looks for that shape everywhere in the template, so the next one
gets caught before it ships.
"""

import json
import re

from pathlib import Path

TEMPLATE_ROOT = Path(__file__).parent.parent / "src" / "scicookie"
PROJECT_TEMPLATE = TEMPLATE_ROOT / "{{cookiecutter.project_slug}}"
HOOKS = TEMPLATE_ROOT / "hooks"
REPO_ROOT = TEMPLATE_ROOT.parent.parent

EQUALITY = re.compile(
    r"cookiecutter\.([a-zA-Z_][a-zA-Z0-9_]*)\s*(?:==|!=)\s*"
    r"([\"'])(.*?)\2"
)
MEMBERSHIP = re.compile(
    r"cookiecutter\.([a-zA-Z_][a-zA-Z0-9_]*)\s+(?:not\s+in|in)\s*"
    r"\[([^\]]*)\]"
)
STRING_LITERAL = re.compile(r"[\"'](.*?)[\"']")

# Known cases that are already being fixed elsewhere, as
# (file name, variable, value). Each entry is checked below, so when the
# other fix lands this test fails and tells you to delete the entry.
KNOWN_PENDING = {
    # release.yaml compares documentation_engine against "sphinx", but the
    # real values are "sphinx(rst)" and "sphinx(myst)". See issue #380.
    ("release.yaml", "documentation_engine", "sphinx"),
}


def _choice_domains():
    """Return every cookiecutter variable that has a fixed list of choices."""
    config = json.loads((TEMPLATE_ROOT / "cookiecutter.json").read_text())
    return {
        name: values
        for name, values in config.items()
        if isinstance(values, list) and not name.startswith("_")
    }


def _template_files():
    """Yield every file in the hooks and in the project template."""
    for root in (HOOKS, PROJECT_TEMPLATE):
        for path in sorted(root.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                yield path


def _comparisons():
    """Yield (path, line number, variable, value) for each comparison."""
    for path in _template_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(text.splitlines(), start=1):
            for name, _quote, value in EQUALITY.findall(line):
                yield path, number, name, value
            for name, body in MEMBERSHIP.findall(line):
                for value in STRING_LITERAL.findall(body):
                    yield path, number, name, value


def test_choice_comparisons_use_a_real_choice():
    """Reject conditionals comparing a variable to a value it never has."""
    domains = _choice_domains()
    unreachable = []
    seen_pending = set()

    for path, number, name, value in _comparisons():
        if name not in domains or value in domains[name]:
            continue

        key = (path.name, name, value)
        if key in KNOWN_PENDING:
            seen_pending.add(key)
            continue

        unreachable.append(
            f"{path.relative_to(REPO_ROOT)}:{number}: "
            f"cookiecutter.{name} is compared with {value!r}, "
            f"which is not one of {domains[name]}"
        )

    assert not unreachable, "unreachable conditional branch(es):\n" + (
        "\n".join(unreachable)
    )

    fixed = KNOWN_PENDING - seen_pending
    assert not fixed, (
        "these entries are fixed now and should be removed from "
        f"KNOWN_PENDING: {sorted(fixed)}"
    )
