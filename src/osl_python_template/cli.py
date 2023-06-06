import argparse

import inquirer
from colorama import Fore, Style


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="osl-python-template",
        description="CLI tool for calling cookieninja",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete and re-download the template",
    )
    return parser.parse_args()


def prompt_questions():
    questions = [
        inquirer.Confirm(
            "delete",
            message="You've downloaded /home/xmn/"
            + ".cookiecutters/cookiecutter-python before."
            "Is it okay to delete and re-download it?",
            default=True,
        ),
        inquirer.Text(
            "author_name", message="Author's name", default="Roronoa Zoro"
        ),
        inquirer.Text(
            "author_email", message="Author's email", default="zoro@one.piece"
        ),
        inquirer.Text(
            "project_name",
            message="Project name, the title of the project",
            default="OSL Python package",
        ),
        inquirer.Text(
            "project_description",
            message="Project short description",
            default="OSL Python Package contains all the "
            + "boilerplate you need to create a Python package.",
        ),
        inquirer.Text(
            "project_slug",
            message="Project Slug, the code name for your project",
            default="pyopensci-template",
        ),
        inquirer.Text(
            "package_slug",
            message="Package slug, the code name for your package",
            default="pyopensci_template",
        ),
        inquirer.Text(
            "project_version", message="Project version", default="0.1.0"
        ),
        inquirer.Text(
            "project_url",
            message="Project URL",
            default="https://pyopensci-template.com",
        ),
        inquirer.List(
            "license_name",
            message="Select the project license",
            choices=[
                "MIT",
                "BSD 3 Clause",
                "ISC license",
                "Apache Software License 2.0",
                "GNU General Public License v3",
                "Other",
            ],
        ),
        inquirer.Text("license_url", message="License URL", default=""),
        inquirer.List(
            "project_layout",
            message="Select the project layout",
            choices=["src layout", "flat layout"],
        ),
        inquirer.List(
            "cli",
            message="Select the Command Line Interface (CLI)",
            choices=["Click", "Argparse", "docopt", "Typer", "No CLI"],
        ),
        inquirer.List(
            "doc_engine",
            message="Select the Documentation Engine",
            choices=["MkDocs", "Sphinx", "Quarto"],
        ),
        inquirer.Text(
            "doc_template",
            message="Select the template for the Documentation Engine",
            default="Material",
        ),
        inquirer.List(
            "test_library",
            message="Select the test library",
            choices=["pytest", "hyphotesis", "unittest"],
        ),
        inquirer.List(
            "code_of_conduct",
            message="Select Code of Conduct",
            choices=[
                "Contributor Covenant (projects of all sizes)",
                "Citizen Code of Conduct (communities and events)",
                "None",
            ],
        ),
        inquirer.List(
            "governance_document",
            message="Select a governance document template",
            choices=[
                "NumPy governance document",
                "SciML governance document",
                "None",
            ],
        ),
        inquirer.List(
            "roadmap_document",
            message="Select a Roadmap document template",
            choices=["PyTorch-Ignite roadmap document", "None"],
        ),
        inquirer.Checkbox(
            "initial_tools",
            message="Select the initial tools you want to add to your project",
            choices=[
                "blue",
                "black",
                "shellcheck",
                "bandit",
                "pydocstyle",
                "vulture",
                "mccabe",
            ],
            default=["blue", "black", "shellcheck"],
        ),
        inquirer.List(
            "container_tech",
            message="Select the container technology for this project",
            choices=["None", "Docker", "Podman", "kubernetes"],
        ),
        inquirer.Confirm(
            "configure_git",
            message="Configure the local git repository?",
            default=True,
        ),
        inquirer.Text(
            "git_username", message="Git username", default="zoro_roronoa"
        ),
        inquirer.Text(
            "git_https_origin", message="Git https origin URL", default=""
        ),
        inquirer.Text(
            "git_https_upstream", message="Git https upstream URL", default=""
        ),
        inquirer.Text(
            "git_main_branch", message="Git main branch", default="main"
        ),
        inquirer.Confirm(
            "configure_pypi",
            message="Configure the PyPI username?",
            default=True,
        ),
        inquirer.Text(
            "pypi_username", message="PyPI username", default="zoro_roronoa"
        ),
    ]
    answers = inquirer.prompt(questions)
    return answers


def main():
    args = parse_arguments()

    if args.delete:
        print("You've chosen to delete and re-download the template.")

    answers = prompt_questions()

    # Print the answers
    print(Fore.GREEN + "\nYour answers:" + Style.RESET_ALL)
    for key, value in answers.items():
        print(f"{key}: {value}")



