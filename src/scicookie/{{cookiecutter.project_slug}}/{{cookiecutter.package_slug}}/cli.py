"""Module with CLI functions."""

{%- if cookiecutter.use_black == "yes" %}
  {%- set QUOTE = '"' -%}
{%- else %}
  {%- set QUOTE = "'" -%}
{%- endif %}

{%- if cookiecutter.command_line_interface == "Argparse" %}

import argparse
import os
import sys

from {{ cookiecutter.package_slug }} import  __version__


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
        prog={{ QUOTE }}{{ cookiecutter.project_slug }}{{ QUOTE }},
        description=({{ QUOTE }}{{ cookiecutter.project_name }}{{ QUOTE }}),
        epilog=(
            {{ QUOTE }} If you have any problem, open an issue at: {{ QUOTE }}
            {{ QUOTE }}{{ cookiecutter.project_url }}{{ QUOTE }}
        ),
        add_help=True,
        formatter_class=CustomHelpFormatter,
    )
    parser.add_argument(
        {{ QUOTE }}--version{{ QUOTE }},
        action={{ QUOTE }}store_true{{ QUOTE }},
        help={{ QUOTE }}Show the version of the installed {{ cookiecutter.project_name }} tool.{{ QUOTE }},
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

{%- else cookiecutter.command_line_interface == "Click" %}

import click

from {{ cookiecutter.package_slug }} import __version__

@click.command()
@click.option({{ QUOTE }}--version{{ QUOTE }}, is_flag=True, help={{ QUOTE }}Show the version of the installed {{ cookiecutter.project_name }} tool.{{ QUOTE }})

def app(version):
    """Run the application."""
    if version:
        return click.echo(__version__)
    click.echo("You can add more Click commands here.")

if __name__ == {{ QUOTE }}__main__{{ QUOTE }}:
    app()

{%- endif %}
