![LOGO](/images/logo.png)

{% set is_open_source = cookiecutter.project_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* License: {{ cookiecutter.project_license }}
* Documentation: https://{{ cookiecutter.project_slug }}.github.io
{% endif %}

## Features

{% if cookiecutter.project_layout == "src" -%}
* src layout: Is a good practice moving the Python code that is
  intended to be importable of your package in a *src* directory. This
  package structure is technically called a “regular package” in Python,
  and it is what the vast majority of Python packages and developers
  use.
{% else %}
* flat layout: refers to organising a project's files in a folder
  or repository so that the various configuration files and import
  packages are all in the top-level directory.
{% endif -%}

{%- if cookiecutter.use_bandit in ["yes", "y"] %}
* The security of our code: Bandit is a powerful tool that we use in our Python
  project to ensure its security. This tool analyzes the code and detects
  potential vulnerabilities. Some of the key features of Bandit are its ease of
  use, its ability to integrate with other tools, and its support for multiple
  Python versions. If you want to know about bandit you can check its
  [documentation](https://bandit.readthedocs.io/en/latest/).
{% endif -%}

{% if cookiecutter.use_pydocstyle == 'yes' %}
- This package uses [pydocstyle](http://www.pydocstyle.org/en/stable/)
  for checking compliance with Python documentation conventions.
{% endif %}

{% if cookiecutter.use_vulture == 'yes' %}
* Finds unused code: [Vulture](https://github.com/jendrikseipp/vulture)
  is useful for cleaning up and finding errors in large code bases in
  Python.
{%- endif %}

* TODO

## Credits

This package was created with Cookieninja and the
[osl-incubator/cookiecutter-python](https://github.com/osl-incubator/cookiecutter-python)
project template.
