"""
Entrypoint module, in case you use `python -m {{ cookiecutter.project_slug }}`.

Why does this file exist, and why __main__? For more info, read:
- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""
{%- if cookiecutter.use_blue %}
  {%- set QUOTE = "'" -%}
{%- elif cookiecutter.use_black %}
  {%- set QUOTE = '"' -%}
{%- else %}
  {%- set QUOTE = "'" -%}
{%- endif %}

from {{cookiecutter.package_slug}}.cli import main  # type: ignore, noqa: E402

if __name__ == {{ QUOTE }}__main__{{ QUOTE }}:
    main()
