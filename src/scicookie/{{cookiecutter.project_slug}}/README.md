{% set is_open_source = cookiecutter.project_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source -%}
* Free software: {{ cookiecutter.project_license }}
* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.io.
{%- endif %}

## Features
{% if cookiecutter.build_system == "poetry" %}
* Build system: We use [Poetry](https://python-poetry.org/), it's a Python
package management tool that simplifies the process of building and publishing
Python packages. It allows us to easily manage dependencies, virtual
environments and package versions. Poetry also includes features such as
dependency resolution, lock files and publishing to PyPI. Overall, Poetry
streamlines the process of managing Python packages, making it easier for us to
create and share our code with others.
{%- elif cookiecutter.build_system == "flit" %}
* Build system: We use [Flit](https://flit.pypa.io), it's a Python package that
simplifies the process of publishing Python packages. It allows us to easily
create and publish our packages to PyPI. Flit handles the packaging,
distribution, and installation of Python packages, making it easier for us to
share our code with others. It also includes features such as dependency
management, versioning, and metadata management.
{%+ endif -%}
{%- if cookiecutter.use_bandit == "yes" %}
* The security of our code: Bandit is a powerful tool that we use in our Python
  project to ensure its security. This tool analyzes the code and detects
  potential vulnerabilities. Some of the key features of Bandit are its ease of
  use, its ability to integrate with other tools, and its support for multiple
  Python versions. If you want to know about bandit you can check its
  [documentation](https://bandit.readthedocs.io/en/latest/).
{%+ endif -%}
{%- if cookiecutter.use_pydocstyle == "yes" %}
* This package uses [pydocstyle](http://www.pydocstyle.org/en/stable/)
  for checking compliance with Python documentation conventions.
{%+ endif -%}
{%- if cookiecutter.use_vulture == "yes" %}
* Finds unused code: [Vulture](https://github.com/jendrikseipp/vulture)
  is useful for cleaning up and finding errors in large code bases in
  Python.
{%+ endif -%}
{%- if cookiecutter.use_mccabe == "yes" %}
* Complexity of functions and modules: We use
[McCabe](https://github.com/PyCQA/mccabe) to identify the complexity in our
Python code that may be difficult to maintain or understand. By identifying
complex code at the outset, we as developers can refactor it to make it easier
to maintain and understand. In summary, McCabe helps us to improve the quality
of our code and make it easier to maintain. If you would like to learn more
about McCabe and code complexity, you can visit [McCabe - Code Complexity
Checker](https://here-be-pythons.readthedocs.io/en/latest/python/mccabe.html).
This tool is included with [Flake8](https://flake8.pycqa.org/en/latest/).
{%+ endif -%}
{%- if cookiecutter.use_containers == 'Docker' %}
* Integration with DevOps tools: We use Docker because it allows us to create an
  isolated environment for our application that includes all the necessary
  dependencies, libraries and configurations. This makes it easier to manage and
  reproduce our development and production environments without any conflicts or
  inconsistencies.

  With Docker, we can easily share our application with others and deploy it to
  different environments. This streamlines our development, testing, deployment,
  and collaboration workflows, making the entire process more efficient.
{%- elif cookiecutter.use_containers == 'Podman' %}
* Integration with DevOps tools: Podman in your Python project helps us
  achieve a more secure, efficient, and flexible containerization strategy, and
  give us more control over application's dependencies and configurations.
  Podman allows us to manage containers without the need for a daemon, providing a
  more secure and lightweight solution.

  With Podman, we can easily create and run containers, as well as manage their
  lifecycle and resources. This integration has improved our development and
  deployment processes, making them more efficient and streamlined.
{%+ endif %}
* TODO

## Credits

This package was created with Cookieninja and the `osl-incubator/scicookie` project template.
