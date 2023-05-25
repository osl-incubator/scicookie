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
* This package uses [pydocstyle](http://www.pydocstyle.org/en/stable/)
  for checking compliance with Python documentation conventions.
{% endif %}

{% if cookiecutter.use_vulture == 'yes' %}
* Finds unused code: [Vulture](https://github.com/jendrikseipp/vulture)
  is useful for cleaning up and finding errors in large code bases in
  Python.
{%- endif %}

{% if cookiecutter.use_mccabe in ['yes', 'y'] -%}
* Complexity of functions and modules: We use
[McCabe](https://github.com/PyCQA/mccabe) to identify the complexity in our
Python code that may be difficult to maintain or understand. By identifying
complex code at the outset, we as developers can refactor it to make it easier
to maintain and understand. In summary, McCabe helps us to improve the quality
of our code and make it easier to maintain. If you would like to learn more
about McCabe and code complexity, you can visit [McCabe - Code Complexity
Checker](https://here-be-pythons.readthedocs.io/en/latest/python/mccabe.html).
This tool is included with [Flake8](https://flake8.pycqa.org/en/latest/).
{%- endif %}

* TODO

## Credits

This package was created with Cookieninja and the `osl-incubator/cookiecutter-python` project template.
