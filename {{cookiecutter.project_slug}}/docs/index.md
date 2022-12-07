![LOGO](/images/logo.png)

{% set is_open_source = cookiecutter.project_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* License: {{ cookiecutter.project_license }}
* Documentation: https://{{ cookiecutter.project_slug }}.github.io
{% endif %}

## Features

* TODO

## Credits

This package was created with Cookiecutter and the
[osl-incubator/cookiecutter-python](https://github.com/osl-incubator/cookiecutter-python)
project template.
