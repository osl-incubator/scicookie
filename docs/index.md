# SciCookie

![CI](https://img.shields.io/github/actions/workflow/status/osl-incubator/scicookie/main.yaml?logo=github&label=CI)
[![Python Versions](https://img.shields.io/pypi/pyversions/scicookie)](https://pypi.org/project/scicookie/)
[![Package Version](https://img.shields.io/pypi/v/scicookie?color=blue)](https://pypi.org/project/scicookie/)
![License](https://img.shields.io/pypi/l/scicookie?color=blue)
![Discord](https://img.shields.io/discord/796786891798085652?logo=discord&color=blue)

**SciCookie** is a template developed by
[Open Science Labs](https://opensciencelabs.org/) that creates projects from
project templates and is based on
[Cookiecutter](https://github.com/cookiecutter/cookiecutter). It serves as an
initial structure which can be used by beginners as well as full-fledged
developers to simplify the project creation process and save considerable amount
of time. SciCookie enables projects with an initial layout that includes
recommended tools, workflows, and project structure.

Cookiecutter also offers other features that can enhance the workflow of the
development process. Features such as _automatic documentation generation,
automated testing,_ and _project-specific configuration_ are part of this.
Overall, Cookiecutter is an efficient tool that gives users the ability to
effortlessly create consistent, high-quality projects.

Open Science Labs Scientific Python cookiecutter template is primarily based on
the **PyOpenSci** recommendations who is actively conducting research to
determine the tools, libraries, best practices, and workflows utilized by
significant scientific Python groups. As a result, this template offers to
authors a starting point for their project that adheres with industry standards
and can be adjusted to meet particular project requirements.

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a
Python package.

- GitHub repo: <https://github.com/osl-incubator/scicookie/>
- Software License: BSD license

## Features

- Allows package slug (use `_` instead of `-`)
- Licenses supported: MIT, BSD 3 Clause, ISC License, Apache Software License
  2.0, and GPL 3
- Documentation engines: mkdocs, sphinx-rst, sphinx-myst, jupyter-boook, quarto
- Test library: pytest, hypothesis
- Auto format code tools: _black_, _ruff_ and _prettier_.
- Code style with _Flake8_.
- Allows _Ruff_ to be used as a linter.
- Initial integration with git
- Support to conda (as base environment) and poetry as packaging and dependency
  management
- Support to pre-commit
- Static analysis of shell scripts using _ShellCheck_.
- Support for _Makim_ and _Make_ as automation tools.
- You can choose between different code of conduct, roadmap and governance
  documents based on recognized community documents.
- CI options: github actions, circleci, azure pipelines and gitlab CI.
- Release workflow with semantic release
- Flexible build system selection: Choose between popular build systems like
  [Poetry](https://python-poetry.org/), [Flit](https://flit.pypa.io),
  [meson-python](https://meson-python.readthedocs.io/en/latest/index.html),
  [Setuptools](https://setuptools.pypa.io/en/latest/),
  [PDM](https://pdm.fming.dev/), [Hatch](https://hatch.pypa.io),
  [Pixi](https://pixi.sh/latest/), [uv](https://docs.astral.sh/uv/),
  [Maturin](https://pypi.org/project/maturin/0.8.2/),
  [scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/) or
  [setuptools + pybind11](https://pybind11.readthedocs.io/en/stable/) based on
  your preference.
- The structure of the project can use the _src layout_ or _flat layout_. The
  “src layout” moving the code that is intended to be importable into a
  subdirectory. This subdirectory is typically named src. "Flat layout" refers
  to organising a project's files in a folder or repository so that the various
  configuration files and import packages are all in the top-level directory.
  You can read about their differences at
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
- Choose between _Click_ and _Argparse_ as Command Line Interface (CLI)
- Code coverage testing with _Coverage_.
- Provides the option to add initial files that allow you to run and orchestrate
  containers using [Docker](https://docs.docker.com/) (Podman is supported
  through `docker-compose`).

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.0.0):

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

_Use a profile as an alternative_

A profile is a set of template-specific settings. OSL has a specific profile
with the libraries we recommend. You can use it to generate the project by
running:

```bash
scicookie --profile osl
```

**Note**: _If the `--profile osl` flag omitted, the default SciCookie profile
will be used_

You can also use it with `pipx`:

```bash
pipx run scicookie --profile osl
```

## Development

For testing your changes locally, you can run:

```bash
makim tests.lint
makim tests.unit
makim tests.smoke
```

## Maintainers

- Anavelyz Perez - [@Anavelyz](https://github.com/Anavelyz)
- Ankit Kumar - [@ayeankit](https://github.com/ayeankit)
- Ever Vino - [@EverVino](https://github.com/EverVino)
- Ivan Ogasawara - [@xmnlab](https://github.com/xmnlab)
- Saransh Chopra - [@Saransh-cpp](https://github.com/Saransh-cpp)
- Yurely Camacho - [@YurelyCamacho](https://github.com/YurelyCamacho)
