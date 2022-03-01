{% set is_open_source = cookiecutter.open_source_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

## Features

* TODO

## Credits

This package was created with Cookiecutter and the `osl-incubator/cookiecutter-pypackage` project template.
