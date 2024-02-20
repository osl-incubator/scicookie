"""
Entrypoint module, in case you use `python -m {{ cookiecutter.project_slug }}`.

Why does this file exist, and why __main__? For more info, read:
- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""
{%- if cookiecutter.use_black == "yes" %}
  {%- set QUOTE = '"' -%}
{%- else %}
  {%- set QUOTE = "'" -%}
{%- endif %}

from {{cookiecutter.package_slug}}.cli import main  # type: ignore

if __name__ == {{ QUOTE }}__main__{{ QUOTE }}:
    main()
