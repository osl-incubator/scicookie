{% set is_open_source = cookiecutter.project_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source -%}

- Software License: {{ cookiecutter.project_license }}
{%- endif %}
- Documentation: {{ cookiecutter.documentation_url }}

## Features

TBD

## Credits

This package was created with
[scicookie](https://github.com/osl-incubator/scicookie) project template.
