# Cookiecutter Python Package

**SciCookie** is a template developed by [Open Science Labs](https://opensciencelabs.org/) that creates projects from project templates and is based on [Cookieninja](https://github.com/cookieninja-generator/cookieninja) **A Cookiecutter Fork** command-line utility. It serves as a boilerplate which can be used by beginners as well as full fledged developers to simplify the project creation process and save considerable amount of time.
Cookieninja enables projects with an initial layout that includes recommended tools, workflows, and project structure.

Cookieninja also offers other features that can enhance the workflow of the development process. Features such as *automatic documentation generation, automated testing,* and *project-specific configuration* are part of this. Overall, Cookieninja is an efficient tool that gives users the ability to effortlessly create consistent, high-quality projects.

Open Science Labs Scientific Python cookiecutter template is primarily based on the **PyOpenSci** recommendations who is actively conducting research to determine the tools, libraries, best practices, and workflows utilized by significant scientific Python groups. As a result, this template offers to authors a starting point for their project that adheres with industry standards and can be adjusted to meet particular project requirements.


[Cookieninja](https://github.com/cookieninja-generator/cookieninja) template
for a Python package.

  - GitHub repo: <https://github.com/osl-incubator/scicookie/>
  - Free software: BSD license

## Features

  - Allows package slug (use `_` instead of `-`)
  - Licenses supported: MIT, BSD 3 Clause, ISC License, Apache Software License 2.0, and GPL 3
  - Documentation engines: mkdocs, sphinx, jupyter-boook
  - Test library: pytest, hypothesis 
  - Auto format code tool: blue and black
  - Initial integration with git
  - Support to conda (as base environment) and poetry as packaging and dependency management
  - Support to pre-commit
  - CI with github actions
  - Release workflow with semantic release and github actions
  - Flexible build system selection: Choose between popular build
    systems like [Poetry](https://python-poetry.org/),
    [Flit](https://flit.pypa.io),
    [meson-python](https://meson-python.readthedocs.io/en/latest/index.html),
    [Setuptools](https://setuptools.pypa.io/en/latest/),
    [PDM](https://pdm.fming.dev/),
    [Hatch](https://hatch.pypa.io),
    [Maturin](https://pypi.org/project/maturin/0.8.2/),
    [scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/) or
    [setuptools + pybind11](https://pybind11.readthedocs.io/en/stable/)
    based on your preference.
  - The structure of the project can use the *src layout* or *flat
  layout*. The “src layout” moving the code that is intended to be
  importable into a subdirectory. This subdirectory is typically named
  src. "Flat layout" refers to organising a project's files in a folder
  or repository so that the various configuration files and import
  packages are all in the top-level directory. You can read about their differences at
  https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
  - Finding common security problems in Python code using
    [bandit](https://bandit.readthedocs.io/en/latest/)
  - Offers the option to use [pydocstyle](http://www.pydocstyle.org/en/stable/)
  for checking compliance with Python documentation conventions.
  - Finds unused code in Python programs using
    [vulture](https://github.com/jendrikseipp/vulture).
  - To automatically detect overly complex code based on cyclomatic complexity,
    the template gives you the option to use the
    [McCabe](https://github.com/PyCQA/mccabe) library, which is included via
    flake8.
  - Provides the option to add initial files that allow you to run and
    orchestrate containers using [Docker](https://docs.docker.com/) or
    [Podman](https://podman.io/) in your project.

## Quickstart

Install the latest Cookieninja if you haven't installed it yet (this
requires Cookieninja 1.0.0):

```bash
pip install scicookie
```

Go to a desired folder to create your new project, for example:

```bash
cd ~/dev/my-python-projects
```

Generate a Python package project:

```bash
scicookie
```

## Development

For testing your changes locally, you can run:

```bash
makim tests.lint
makim tests.unittest
makim tests.smoke
```

## Maintainers

- Anavelyz Perez - [@Anavelyz](https://github.com/Anavelyz)
- Ever Vino - [@EverVino](https://github.com/EverVino)
- Ivan Ogasawara - [@xmnlab](https://github.com/xmnlab)
- Yurely Camacho - [@YurelyCamacho](https://github.com/YurelyCamacho)
