# Contributing

In order to be able to contribute, it is important that you understand
the project layout.
{% if cookiecutter.project_layout == "src" -%}
This project uses the *src layout*, which means that the package code is located
at `./src/{{ cookiecutter.package_slug }}`.
{% else -%}
This project uses the *flat layout*, which means that the package code is located
at `./{{ cookiecutter.package_slug }}`.
{% endif %}
For my information, check the official documentation:
https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

{% if cookiecutter.build_system == "poetry" -%}
In addition, you should know that to build our package we use
[Poetry](https://python-poetry.org/), it's a Python package management tool that
simplifies the process of building and publishing Python packages. It allows us
to easily manage dependencies, virtual environments and package versions. Poetry
also includes features such as dependency resolution, lock files and publishing
to PyPI. Overall, Poetry streamlines the process of managing Python packages,
making it easier for us to create and share our code with others.
{%- elif cookiecutter.build_system == "flit" -%}
In addition, you should know that to build our package we use
[Flit](https://flit.pypa.io), it's a Python package that simplifies the process
of publishing Python packages. It allows us to easily create and publish our
packages to PyPI. Flit handles the packaging, distribution, and installation of
Python packages, making it easier for us to share our code with others. It also
includes features such as dependency management, versioning, and metadata
management.
{%- elif cookiecutter.build_system == "mesonpy" -%}
In addition, you should know that to build our package we use
[meson-python](https://meson-python.readthedocs.io/en/latest/index.html),
it's a tool for automating and simplifying the construction of software
projects written in the Python programming language. It is based on the
*Meson* build system, which allows you to efficiently configure and manage
the build process of a project. It allows you to easily define project
dependencies, specify build options, generate configuration files and
build scripts, among other tasks related to building software.
{%- elif cookiecutter.build_system == "setuptools" -%}
In addition, you should know that to build our package we use
[Setuptools](https://setuptools.pypa.io/en/latest/), it's a package to easily
define the package structure, manage dependencies and convert our project into a
distributable package. Also, setuptools automates tasks such as packaging
and installation, saving time and effort for both our team and end-users.
{%- elif cookiecutter.build_system == "pdm" -%}
In addition, you should know that to build our package we use
[PDM](https://pdm.fming.dev/), it's a build system for Python projects.
It provides an efficient and fast way to manage project dependencies, as
well as build and distribute code. It is fast to install, has built-in
virtualenv, offers support for different package sources, and provides
an easy way to distribute code.
{%- elif cookiecutter.build_system == "hatch" -%}
In addition, you should know that to build our package we use
[Hatch](https://hatch.pypa.io): It's a Python Package that is compatible build backend used by Hatch, a modern, extensible Python project manager. It provides a standardized build system with reproducible builds by default, robust environment management with support for custom scripts, easy publishing to PyPI or other indexes, version management, and configurable project generation with sane defaults. Hatchling might support multiple programming languages and offer language-specific options for building projects in different languages. It could also provide customization and extensibility options, allowing you to incorporate plugins or scripts for tailored build processes.
{%- elif cookiecutter.build_system == "maturin" -%}
In addition, you should know that to build our package we use
[Maturin](https://pypi.org/project/maturin/0.8.2/):It's a Python packaging tool and build system for creating Python bindings from Rust projects. It enables seamless integration of Rust code into Python applications, offering efficient builds, cross-platform support, and compatibility with different Python versions. Maturin automates the process of generating Python modules that directly call Rust functions, leveraging Rust's performance and low-level capabilities in Python. With its easy-to-use interface and integration with setuptools and Cargo, Maturin provides a straightforward solution for developers seeking to combine the strengths of Python and Rust in a single project.
{%- elif cookiecutter.build_system == "scikit-build-core" -%}
In addition, you should know that to build our package we use
[scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/): It's a Python packaging tool and build system an improved build system generator for CPython C extensions. It provides better support for additional compilers, build systems, cross compilation, and locating dependencies and their associated build requirements.This tool improves package management in the scientific Python ecosystem, enabling cross-platform builds with CMake, and seamless integration with C/C++ libraries for research software engineers.
{%- elif cookiecutter.build_system == "pybind11" -%}
In addition, you should know that to build our package we use
[setuptools + pybind11](https://pybind11.readthedocs.io/en/stable/): It's a Python packaging tool for C++ build system that simplifies creating Python bindings for C++ code, allowing easy integration of C++ functions and classes into Python scripts. Acting as a bridge between the two languages, it enables direct calls to C++ functionality from Python as if it were a native Python module. Its user-friendly syntax reduces boilerplate code, while standard C++ build systems like CMake or Make aid in project compilation. Pybind11's efficiency and strong community support make it a popular choice for projects requiring seamless interoperability between C++ and Python, from scientific computing to game development.

{%- endif %}

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at {{ cookiecutter.git_https_upstream }}/issues.

If you are reporting a bug, please include:

  - Your operating system name and version.
  - Any details about your local setup that might be helpful in
    troubleshooting.
  - Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with “bug” and
“help wanted” is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
“enhancement” and “help wanted” is open to whoever wants to implement
it.

### Write Documentation

{{ cookiecutter.project_name }} could always use more documentation,
whether as part of the official {{ cookiecutter.project_name }} docs,
in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
{{ cookiecutter.git_https_upstream }}/issues.

If you are proposing a feature:

  - Explain in detail how it would work.
  - Keep the scope as narrow as possible, to make it easier to
    implement.
  - Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Get Started!

Ready to contribute? Here’s how to set up `{{ cookiecutter.project_slug}}` for local development.

1.  Fork the `{{ cookiecutter.project_slug }}` repo on GitHub.

2.  Clone your fork locally::

    $ git clone git@github.com:your_name_here/{{ cookiecutter.project_slug }}.git

3.  Install your local copy into a virtualenv. Assuming you have
    virtualenvwrapper installed, this is how you set up your fork for
    local development::

    $ mkvirtualenv {{ cookiecutter.project_slug }}
    $ cd {{cookiecutter.project_slug }}/
    $ python setup.py develop

4.  Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5.  When you’re done making changes, check that your changes pass flake8
    and the tests, including testing other Python versions with tox::

    $ make lint
    $ make test

    To get flake8 and tox, just pip install them into your virtualenv.

6.  Commit your changes and push your branch to GitHub::

    $ git add . $ git commit -m “Your detailed description of your
    changes.” $ git push origin name-of-your-bugfix-or-feature

7.  Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
3.  The pull request should work for Python >= 3.8.

## Tips

To run a subset of tests::
{% if cookiecutter.use_pytest == "yes" -%}
```
$ pytest tests.test_{{ cookiecutter.package_slug }}
```
{%- endif %}
{% if cookiecutter.use_hypothesis == "yes" -%}
```
python -m unittest discover
```
{%- endif %}

## Release

This project uses semantic-release in order to cut a new release
based on the commit-message.

### Commit message format

**semantic-release** uses the commit messages to determine the consumer
impact of changes in the codebase. Following formalized conventions for
commit messages, **semantic-release** automatically determines the next
[semantic version](https://semver.org) number, generates a changelog and
publishes the release.

By default, **semantic-release** uses [Angular Commit Message
Conventions](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format).
The commit message format can be changed with the `preset` or `config`
options_ of the
[@semantic-release/commit-analyzer](https://github.com/semantic-release/commit-analyzer#options)
and
[@semantic-release/release-notes-generator](https://github.com/semantic-release/release-notes-generator#options)
plugins.

Tools such as [commitizen](https://github.com/commitizen/cz-cli) or
[commitlint](https://github.com/conventional-changelog/commitlint) can
be used to help contributors and enforce valid commit messages.

The table below shows which commit message gets you which release type
when `semantic-release` runs (using the default configuration):

| Commit message                                                 | Release type     |
|----------------------------------------------------------------|------------------|
| `fix(pencil): stop graphite breaking when pressure is applied` | Fix Release      |
| `feat(pencil): add 'graphiteWidth' option`                     | Feature Release  |
| `perf(pencil): remove graphiteWidth option`                    | Chore            |
| `BREAKING CHANGE: The graphiteWidth option has been removed`   | Breaking Release |

source:
<https://github.com/semantic-release/semantic-release/blob/master/README.md#commit-message-format>

As this project uses the `squash and merge` strategy, ensure to apply
the commit message format to the PR's title.
