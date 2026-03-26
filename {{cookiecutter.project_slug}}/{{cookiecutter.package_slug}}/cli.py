"""Module with CLI functions."""

{%- if cookiecutter.command_line_interface == "Argparse" %}

import argparse

from {{ cookiecutter.package_slug }} import __version__


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
        super().__init__(
            prog,
            indent_increment=indent_increment,
            max_help_position=max_help_position,
            width=width,
            **kwargs,
        )


def get_args():
    """Return the arguments for the CLI."""
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.project_slug }}",
        description=("{{ cookiecutter.project_name }}"),
        epilog=(
            "If you have any problem, open an issue at: "
            "{{ cookiecutter.project_url }}"
        ),
        add_help=True,
        formatter_class=CustomHelpFormatter,
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the version of the installed {{ cookiecutter.project_name }} tool.",
    )

    return parser


def show_version():
    """Show the version for the application."""
    print(__version__)


def app():
    """Run the application."""
    args_parser = get_args()
    args = args_parser.parse_args()

    if args.version:
        return show_version()

{%- elif cookiecutter.command_line_interface == "Click" %}

import click

from {{ cookiecutter.package_slug }} import __version__


@click.command()
@click.option(
    "--version",
    is_flag=True,
    help="Show the version of the installed {{ cookiecutter.project_name }} tool.",
)
def app(version):
    """Run the application."""
    if version:
        return click.echo(__version__)
    click.echo("You can add more Click commands here.")

{%- endif %}


if __name__ == "__main__":
    app()
