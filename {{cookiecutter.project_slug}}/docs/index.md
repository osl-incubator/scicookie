![LOGO](/images/logo.png)

{% set is_open_source = cookiecutter.project_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* License: {{ cookiecutter.project_license }}
* Documentation: https://{{ cookiecutter.project_slug }}.github.io
{% endif %}

## Features

{% if cookiecutter.use_pydocstyle == 'yes' %}
- This package uses [pydocstyle](http://www.pydocstyle.org/en/stable/)
  for checking compliance with Python documentation conventions.
{% endif %}

* TODO

## Credits

This package was created with Cookieninja and the
[osl-incubator/cookiecutter-python](https://github.com/osl-incubator/cookiecutter-python)
project template.
