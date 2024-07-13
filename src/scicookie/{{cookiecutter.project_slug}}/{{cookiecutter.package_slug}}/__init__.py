"""{{ cookiecutter.project_name }}."""
{%- if cookiecutter.use_black == "yes" %}
  {%- set QUOTE = '"' -%}
{%- else %}
  {%- set QUOTE = "'" -%}
{%- endif %}
{% if cookiecutter.build_system in ["hatch", "pdm", "flit"] -%}
__version__ = {{ QUOTE }}{{ cookiecutter.project_version }}{{ QUOTE }}
{%- else %}
from importlib import metadata as importlib_metadata


def get_version() -> str:
    """Return the program version."""
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        {%- if cookiecutter.release_worlflow == "semantic-release" %}
        return {{ QUOTE }}{{ cookiecutter.project_version }}{{ QUOTE }}  # semantic-release
        {%- endif %}
        {%- if cookiecutter.release_worlflow == "release-please" %}
        return {{ QUOTE }}{{ cookiecutter.project_version }}{{ QUOTE }}  # release-please
        {%- endif %}


version = get_version()

__version__ = version
{%- endif %}
__author__ = {{ QUOTE }}{{ cookiecutter.author_full_name }}{{ QUOTE }}
__email__ = {{ QUOTE }}{{ cookiecutter.author_email }}{{ QUOTE }}
