{% set is_open_source = cookiecutter.project_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.project_license }}
* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.io.
{% endif %}

## Features

{%+ if cookiecutter.use_bandit in ["yes", "y"] -%}
* The security of our code: Bandit is a powerful tool that we use in our Python
  project to ensure its security. This tool analyzes the code and detects
  potential vulnerabilities. Some of the key features of Bandit are its ease of
  use, its ability to integrate with other tools, and its support for multiple
  Python versions. If you want to know about bandit you can check its
  [documentation](https://bandit.readthedocs.io/en/latest/).
{%- endif %}

{% if cookiecutter.use_pydocstyle == 'yes' %}
- This package uses [pydocstyle](http://www.pydocstyle.org/en/stable/)
  for checking compliance with Python documentation conventions.
{% endif %}

* TODO

## Credits

This package was created with Cookieninja and the `osl-incubator/cookiecutter-python` project template.
