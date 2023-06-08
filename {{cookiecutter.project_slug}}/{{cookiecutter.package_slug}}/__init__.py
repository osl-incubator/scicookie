# type: ignore[attr-defined]
"""{{ cookiecutter.project_name }}"""
{%- if cookiecutter.use_blue %}
  {%- set QUOTE = "'" -%}
{%- elif cookiecutter.use_black %}
  {%- set QUOTE = '"' -%}
{%- else %}
  {%- set QUOTE = "'" -%}
{%- endif %}
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return {{ QUOTE }}{{ cookiecutter.project_version }}{{ QUOTE }}  # semantic-release


version: str = get_version()

__author__ = {{ QUOTE }}{{ cookiecutter.author_full_name }}{{ QUOTE }}
__email__ = {{ QUOTE }}{{ cookiecutter.author_email }}{{ QUOTE }}
__version__: str = version
