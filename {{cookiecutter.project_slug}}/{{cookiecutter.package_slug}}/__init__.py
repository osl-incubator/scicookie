"""Top-level package for {{ cookiecutter.project_name }}."""

{%- if cookiecutter.auto_format_tool == 'blue' %}
  {%- set QUOTE = "'" -%}
{%- elif cookiecutter.auto_format_tool == 'black' %}
  {%- set QUOTE = '"' -%}
{%- else %}
  {%- set QUOTE = "'" -%}
{%- endif %}


__author__ = {{ QUOTE }}{{ cookiecutter.author_full_name }}{{ QUOTE }}
__email__ = {{ QUOTE }}{{ cookiecutter.author_email }}{{ QUOTE }}
__version__ = {{ QUOTE }}{{ cookiecutter.project_version }}{{ QUOTE }}  # semantic-release
