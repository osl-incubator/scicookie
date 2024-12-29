![CI](https://img.shields.io/github/actions/workflow/status/osl-incubator/scicookie/main.yaml?logo=github&label=CI)
[![Python Versions](https://img.shields.io/pypi/pyversions/scicookie)](https://pypi.org/project/scicookie/)
[![Package Version](https://img.shields.io/pypi/v/scicookie?color=blue)](https://pypi.org/project/scicookie/)
![License](https://img.shields.io/pypi/l/scicookie?color=blue)
![Discord](https://img.shields.io/discord/796786891798085652?logo=discord&color=blue)

![logo_scicookie.png](https://github.com/osl-incubator/scicookie/blob/main/docs/images/logo_scicookie.png?raw=true)

**SciCookie** is a project template designed to simplify scientific Python
project creation. It provides an initial structure with recommended tools,
workflows, and industry best practices, saving developers time and effort. Built
upon the PyOpenSci recommendations, it offers a foundation that adheres to
scientific Python standards while remaining customizable to specific project
needs.

- [Documentation](https://osl-incubator.github.io/scicookie/)
- [GitHub](https://github.com/osl-incubator/scicookie)
- [PyPI](https://pypi.org/project/scicookie/)
- [License (BSD)](https://github.com/osl-incubator/scicookie/blob/main/LICENSE)

### Key Features

- **Project Structure:** Choose between "src" (code in a subdirectory) and
  "flat" (all files in the top-level directory) layouts.
- **Packaging & Dependencies:** Supports Poetry, Flit, meson-python, setuptools,
  PDM, Hatch, Maturin, scikit-build-core, Pixi, or setuptools + pybind11 for
  flexible build systems.
- **Testing & Linting:** Integrates with pytest and hypothesis (testing), black,
  ruff and prettier (auto-formatting), bandit (security), pydocstyle
  (documentation style), vulture (unused code detection), flake8 (code style),
  ruff (linter), ShellCheck (static analysis of shell scripts), Coverage (code
  coverage testing), and McCabe (cyclomatic complexity analysis) for a robust
  development environment.
- **Version Control & Automation:** Includes initial git integration, conda
  (base environment) support, pre-commit hooks, continuous integration with
  GitHub Actions, CircleCI, Azure Pipelines and GitLab CI, automation with Make
  and Makim, and release workflows with semantic-release.
- **Documentation:** Offers options for mkdocs, sphinx-rst, sphinx-myst,
  jupyter-book or quarto documentation generation.
- **Containerization:** Provides the ability to add initial files for running
  and managing containers using Docker(Podman is supported via
  `docker-compose`).

### Benefits

- **Reduces boilerplate code:** SciCookie eliminates the need to write
  repetitive project setup code, allowing developers to focus on core
  functionality.
- **Ensures consistency:** Enforces a standardized structure, promoting code
  maintainability and collaboration.
- **Adheres to best practices:** Leverages PyOpenSci recommendations for
  efficient scientific Python development.
- **Improves code quality:** Integrates with various testing and linting tools
  for better code hygiene.
- **Automates workflows:** Streamlines processes like documentation generation,
  version control, and continuous integration.

### Getting Started

**Prerequisites**

- Python: Make sure you have Python installed on your system. You can check by
  running `python --version` or `python3 --version` in your terminal. If you
  don't have it, download it from [here](https://www.python.org/downloads/).

**Installation**

- Install Cookiecutter (if not already installed): Open your terminal and run
  the following command: `pip install scicookie`

**Project Creation**

1. Navigate to your desired project directory: Use the `cd` command to navigate
   to the directory where you want to create your new Python package project.
   For example: `cd ~/dev/my-python-projects` (Replace
   `~/dev/my-python-projects` with your preferred directory path.)

2. Generate the project using SciCookie: Once you're in your desired directory,
   run the following command to generate a new Python package project using
   SciCookie: `scicookie`

_(SciCookie will create a new directory structure for your project, including
files and folders commonly used in scientific Python projects. You can now start
editing and customizing your project to fit your specific needs.)_

##### _Use a profile as an alternative_

A profile is a set of template-specific settings. OSL has a specific profile
with the libraries we recommend. You can use it to generate the project by
running:

`scicookie --profile osl`

**Note**: _If the `--profile osl` flag omitted, the default SciCookie profile
will be used_ Another community can also create a specific profile with the
configurations they recommend.

You can also use it with `pipx`:

`pipx run scicookie --profile osl`

### Community

- Join the community, contribute, or seek assistance.
- [Discord](https://discord.gg/huPRh422)
- [File an Issue](https://github.com/osl-incubator/scicookie/issues)
- [Contributors](https://github.com/osl-incubator/scicookie/graphs/contributors)
- [Contribution Guide](https://github.com/osl-incubator/scicookie/blob/main/docs/contributing.md)
- [Tutorial](https://youtu.be/GozNb4i47Ds?si=MIqJC56Ernvxpj_i)

### Support

- Star us on [GitHub](https://github.com/osl-incubator/scicookie).
- Stay tuned for upcoming support options.
