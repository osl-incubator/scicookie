# SciCookie user guide

SciCookie is a package that offers a template for your Python project. The team
has created this guide to help you understand every option and its
functionality.

The structure of the guide is as follows:

- [SciCookie user guide](#scicookie-user-guide)
  - [Notes about the text-based user interface (TUI)](#notes-about-the-text-based-user-interface-tui)
  - [The author of project](#the-author-of-project)
  - [Information about the project](#information-about-the-project)
  - [Project settings](#project-settings)
    - [Project layout](#project-layout)
    - [Build system](#build-system)
    - [Command-line interfaces (CLIs)](#command-line-interfaces-clis)
    - [Documentation engine](#documentation-engine)
  - [Project tools](#project-tools)
    - [Virtual environment](#virtual-environment)
    - [Code formatter](#code-formatter)
    - [Code security vulnerabilities](#code-security-vulnerabilities)
    - [Code coverage testing](#code-coverage-testing)
    - [Code style and logic (code quality)](#code-style-and-logic-code-quality)
    - [Testing framework](#testing-framework)
    - [Static analysis of shell scripts](#static-analysis-of-shell-scripts)
    - [Pre-commit verification](#pre-commit-verification)
  - [Integration with DevOps tools](#integration-with-devops-tools)
  - [Automation tools](#automation-tools)
  - [Project team](#project-team)
    - [Code of conduct](#code-of-conduct)
    - [Governance document](#governance-document)
    - [Roadmap document](#roadmap-document)
  - [Version control](#version-control)

## Notes about the text-based user interface (TUI)

A TUI, or text-based user interface, is a type of user interface that uses text
and keyboard input to display and interact with information on a computer
screen.

When you run the `scicookie` command in your terminal, a text-based user
interface (TUI) is displayed where you can provide information about the author
or the project itself. You can also choose from several options that are
presented to you, with default values in all cases. To switch from one option to
another, simply press "Enter".

In some cases, you may see a list of sub-options within a main option. Use the
arrow keys to move up and down between the sub-options and the `>` symbol will
appear before the sub-option you have selected. Make sure you press "Enter" to
confirm your selection when the required sub-option has been selected.

You will also see a list of options for the project tools, this is presented in
the following way:

```python
 > [ ] bandit
   [ ] black
   [ ] conda
   [ ] coverage
   [ ] flake8
   [ ] ruff_linter
   [ ] ruff_formatter
   [ ] isort
   [ ] make
   [ ] makim
   [ ] mccabe
   [ ] mypy
   [ ] pre-commit
   [ ] prettier
   [ ] pydocstyle
   [ ] pytest
   [ ] hypothesis
   [ ] shellcheck
   [ ] vulture
```

Use the right arrow key to select the tools you want, and use the up and down
arrow keys to navigate through the list. If you accidentally select an option
you don't want, simply use the left arrow key to deselect it.

The following is a description of the options in the TUI.

## The author of project

With SciCookie, you can easily add information about the author of the project
by filling in the **author_full_name** and **author_email** fields, which refer
to the name and email address of the person or organization that authored the
project.

The default values give you an idea of what you can enter in these fields. This
information can be found in the `pyproject.toml` file, the documentation and the
github configuration, to name a few.

## Information about the project

Every project needs specific information for both development and maintenance.
SciCookie allows you to customise this information, which is displayed in
several parts, such as: documentation, git, configuration files, the project
repository, PyPI (Python Package Index) and more.

Below are the fields within the TUI that relate to project information:

- **project_name**: This is the name of the project according to the creator,
  i.e. the main title of the project, as shown on the README page, for example.

- **project_slug**: This is the name of the project, probably abbreviated using
  characters suitable for naming a Python package. Also, it is the name used for
  the repository and the one registered with PyPI. In simpler terms, it refers
  to the name of the python package to use when you want to install it. In
  SciCookie, this name can include hyphens (-) or underscores (\_).

- **package_slug**: This refers to the name used when importing the package.
  This name allows the usage of (\_) instead of (-), which is a particularity of
  SciCookie. Consequently, the _project_slug_ and the _package_slug_ can match
  (when both use underscores).

- **project_version**: This is where you can enter the version of your python
  package, most Python packages use semantic versioning. SciCookie offers you to
  manage the release workflow with semantic release and github actions. For more
  information on releasing and versioning, please click
  [here](https://py-pkgs.org/07-releasing-versioning.html).

- **project_url**: This is the URL of the project's website used for example, in
  the documentation and the `pyproject.toml` file. On this website you will
  generally find information about the project, the team, events, the blog, etc.
  It is used to promote the project.

- **project_license**: This field allows you to specify the license of the
  project. In SciCookie you can find and choose from the following well-known
  open source software licenses: _MIT_, _BSD 3 Clauses_, _ISC license_, _Apache
  Software License 2.0_ and _GNU General Public License v3_.

  - **`MIT` option**: is a free software license that allows users to use,
    modify and redistribute the software without significant restrictions. It is
    a permissive license that allows users to do whatever they want with the
    software, as long as a copy of the license is included and the original
    authorship of the software is acknowledged. In SciCookie this is the license
    type for default. If you want to know the content of this license, you can
    visit https://mit-license.org/.

  - **`BSD 3 Clauses` option**: also allows users to use, modify and
    redistribute the software without significant restrictions. It is similar to
    the MIT license in terms of permissibility, but includes three additional
    clauses that require you to include a copy of the license, acknowledge
    original authorship of the software, and release the author from any
    liability for damages. For more information, see
    https://opensource.org/license/bsd-3-clause/.

  - **`ISC license` option**: is mainly used to distribute software related to
    networking and Internet protocols. It is permissive and known to be short
    and easy to understand. The author is not responsible for any damage or
    problems caused by the use of the software. You can learn more about the
    contents of this license at https://opensource.org/license/isc-license-txt/.

  - **`Apache Software License 2.0` option**: is a permissive license,
    compatible with the GNU General Public License (GPL). It contains special
    provisions relating to patents. It also requires that copyright and
    attribution notices of the original authors be maintained on all copies of
    the software, and allows users to make modifications to the software and
    distribute modified versions. You can find out more about this license at
    https://www.apache.org/licenses/LICENSE-2.0.

  - **`GNU General Public License v3` option**: includes the freedom to use,
    modify and redistribute the software in accordance with the terms of the
    license. Compared to previous versions, it addresses concerns about
    interoperability with other systems and the use of technological protection
    measures. If you modify or distribute the software under the GPL v3, you
    must make the source code available to end users. More information is
    available at https://www.gnu.org/licenses/gpl-3.0.html.

  If you want to include another type of license according to the needs of your
  project, you can do so by selecting the option `Other`.

## Project settings

Setting up some configurations in the project structure is important because it
allows you to get an orderly workflow. With SciCookie you can configure elements
such as project layout, build system, command-line interface and documentation
engine. This can help streamline the development process by providing a
consistent and standardized framework for the project.

### Project layout

The organization of your code is important, which is why at SciCookie we offer
two alternatives: _src_ and _flat_.

- **src (Source) layout**: The src layout is a common approach where the source
  code files are organized within a dedicated "src" directory. This directory
  serves as the root of the project's source code and typically contains
  subdirectories that represent different modules or packages. Each module or
  package within the "src" directory focuses on a specific aspect of the
  project's functionality.

  For example, a project following the src structure might have the following
  layout:

  ```python
  project_slug/
  ├─ src/
  │  └─ package_slug/
  │     ├─ __init__.py
  |     ├─ __main__.py
  │     ├─ module.py
  │     └─ ...
  ├─ tests
  │  └─ ...
  ├── pyproject.toml
  └── README.md
  ```

  The src structure helps in organizing the codebase and makes it easier to
  understand and maintain as the project grows larger. It also allows for better
  separation of concerns and promotes modularity.

- **Flat layout**: The flat layout involves placing all the project's source
  code files directly in the project's root directory without any
  subdirectories. This means that all modules and packages are at the same level
  and there is no explicit separation between different aspects of the project.

  Here's an example of a flat structure:

  ```python
  project_slug/
  │ └─ package_slug/
  │ __init__.py
  | __main__.py
  │ module.py
  │ ...
  ├─ tests
  │  └─ ...
  ├── pyproject.toml
  └── README.md
  ```

  Because all source files are on the same level in this layout, they are easy
  to find and access. However, as the project becomes larger and more complex,
  it can become more difficult to maintain and navigate the codebase.

  The flat structure is simpler and may be suitable for smaller projects or
  scripts where the codebase is relatively small and does not require extensive
  organization or separation of concerns.

Both **src** and **flat** layouts have their own advantages and disadvantages.
The choice between them depends on your specific requirements and the complexity
of your project, as well as your personal preferences and team conventions.

If you want to find more information about it you can visit:

- [Python Packaging User Guide » Discussions » src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [The source layout](https://py-pkgs.org/04-package-structure.html#the-source-layout)
  in the book [Python Packages](https://py-pkgs.org/) by
  [Tomas Beuzen](https://www.tomasbeuzen.com/) &
  [Tiffany Timbers](https://www.tiffanytimbers.com/).
- [Packaging a python library](https://blog.ionelmc.ro/2014/05/25/python-packaging/)

### Build system

There are several build system options available to development of Python
packages. SciCookie support the following:

- [**Poetry**](https://python-poetry.org/) (default): It's a Python package
  manager that streamlines dependency management and package distribution. It
  provides a simple and intuitive syntax for defining project dependencies and
  allows you to easily create and manage virtual environments for your projects.
  With Poetry, you can easily install, update, and remove dependencies, and it
  automatically handles conflicts and resolution between packages. Additionally,
  Poetry provides a comprehensive toolset for packaging and publishing your
  projects to PyPI, including support for building source distributions and
  wheel packages, as well as generating and uploading documentation. Overall,
  Poetry simplifies the development and distribution of Python projects, making
  it a popular tool for many Python developers.

- [**Flit**](https://flit.pypa.io): It's a Python package and a lightweight tool
  for creating and distributing Python packages. It automates the processes
  involved in packaging and submitting a project to PyPI, and provides a
  straightforward interface for managing a project's dependencies. With just a
  few commands, you can use Flit to quickly create source distributions and
  wheel packages and submit them to PyPI.

- [**meson-python**](https://meson-python.readthedocs.io/en/latest/index.html):
  It's a Python build backend built on top of the _Meson_ build-system. It
  enables you to use Meson for your Python packages. With meson-python, you can
  easily define project dependencies, specify build options, generate
  configuration files and build scripts, among other things. Meson-python is
  primarily focused on improving speed and ease of use compared to other build
  systems. It is designed to be fast and scalable, making it suitable for both
  small and large projects.

- [**Setuptools**](https://setuptools.pypa.io/en/latest/): It's a package that
  facilitates the distribution and installation of Python packages. Setuptools
  provides a way to define metadata about your project, such as its name,
  version, dependencies, and other details. It also provides functionality for
  building and distributing packages, creating distribution archives, and
  installing packages with their dependencies. _"It helps developers to easily
  share reusable code (in the form of a library) and programs (e.g., CLI/GUI
  tools implemented in Python), that can be installed with pip and uploaded to
  PyPI."_

- [**PDM**](https://pdm.fming.dev/): It's a modern Python package and dependency
  manager supporting the latest PEP standards. But it is more than a package
  manager. It boosts your development workflow in various aspects. It has very
  powerful features, including easy and fast dependency resolution, especially
  for large binary distributions, a PEP 517 compilation backend, PEP 621 project
  metadata, a flexible and powerful plugin system. It also offers, among other
  things, versatile user scripting, PyPI integration and version management.

- [**Hatch**](https://hatch.pypa.io): It's a PEP 517/PEP 660 compatible build
  backend used by Hatch, a modern, extensible Python project manager. It
  provides a standardized build system with reproducible builds by default,
  robust environment management with support for custom scripts, easy publishing
  to PyPI or other indexes, version management, and configurable project
  generation with sane defaults. Hatchling ensures that your builds are
  reproducible, so you can be confident that they will always produce the same
  results. It also helps you manage your Python environments, so you can be sure
  that your projects have the correct dependencies.

- [**Maturin**](https://pypi.org/project/maturin/0.8.2/): It's build system
  designed to create Python bindings from Rust projects. It allows Rust code to
  be seamlessly integrated into Python applications, providing efficient builds
  and cross-platform support for various Python versions. Maturin automates the
  generation of Python modules that directly access Rust functions, harnessing
  Rust's high performance and low-level capabilities within Python. Its
  user-friendly interface and compatibility with setuptools and Cargo make it an
  easy-to-use tool, offering developers a simple solution to combine the
  strengths of Python and Rust within a unified project.

- [**scikit-build-core**](https://scikit-build-core.readthedocs.io/en/latest/):
  It's build system designed for Python packaging tool, serving as an enhanced
  build system generator for CPython C extensions greatly improves package
  management within the scientific Python ecosystem. It offers superior support
  for diverse compilers, build systems, cross-compilation, and efficient
  dependency locating with their associated build requirements. With its
  capabilities, it facilitates cross-platform builds using CMake and effortless
  integration with C/C++ libraries, making it a valuable asset for research
  software engineers.

- [**setuptools + pybind11**](https://pybind11.readthedocs.io/en/stable/): It's
  build system designed for C++ library that simplifies the creation of Python
  bindings for C++ code, enabling easy integration of C++ functions and classes
  into Python scripts. It acts as a bridge between the two languages, allowing
  C++ algorithms and functionality to be directly called from Python as if they
  were native Python modules. Pybind11's user-friendly syntax reduces
  boilerplate code, making binding generation more straightforward, while
  standard C++ build systems like CMake or Make facilitate the compilation of
  projects using pybind11. Its efficiency, ease of use, and strong community
  support have made it a popular choice for projects requiring seamless
  interoperability between C++ and Python, ranging from scientific computing to
  game development and automation. Staying up-to-date with the latest pybind11
  documentation ensures the best practices are followed.

- [**Pixi**](https://pixi.sh/latest/): Pixi is a package manager designed to
  simplify dependency management by creating reproducible development
  environments. Pixi focuses on local environments for specific projects,
  generating automatic lock-files to ensure that the same dependencies can be
  installed across different machines. It also offers a cross-platform task
  system for efficient project-specific tasks, such as building, testing, and
  more. Pixi supports multiple languages and is designed to make it easy for
  developers to share their projects without worrying about dependency
  conflicts.

The idea behind the options in SciCookie is that you can choose from some of the
most popular system compilers to suit your needs and preferences for developing
Python packages. If you think we should add more options, you can submit your
suggestion as a issue at
https://github.com/osl-incubator/scicookie/issues/new/choose.

### Command-line interfaces (CLIs)

A command line interface (CLI) is a type of text-based interface that allows the
user to interact with a program or system using text commands rather than a
graphical interface. It allows automation of tasks, access to advanced
functions, and execution of complex commands with additional options.

In addition to the operating system's native CLI, many programs and tools
provide their own command line interfaces to facilitate interaction with their
functionality. With SciCookie you have two CLI options: _Click_ and _Argparse_.

- [**Click**](https://click.palletsprojects.com/en/8.1.x/): The _Command Line
  Interface Creation Kit_ is a Python package that allows you to create
  beautiful command line interfaces in a composable way with as little code as
  necessary. It is highly configurable, it aims to make the process of writing
  command line tools quick and fun.

- [**Argparse**](https://docs.python.org/3/library/argparse.html): This is the
  recommended command line parsing module in the Python standard library, and
  provides an easy way to create command line interfaces with custom arguments
  and options. It helps you parse user-supplied arguments and options, and
  automatically generate help and usage messages.

If you do not want to include a CLI in your project, select
`No command-line interface` (this is the default option).

### Documentation engine

One of the most important elements of a package (apart from the functionality of
the code) is its documentation. If there is no quality documentation, it is very
likely that people will not understand and therefore not use your package.

To generate documentation for any project, tools have been developed that
include functions such as content creation and editing, organization and
classification of information, generation of output formats and integration with
other development and project management tools, known as a **documentation
engine**. This tool automates the creation of technical documentation for
software projects by extracting information from source code, comments and
project metadata.

Depending on your taste and the needs of your project, you should choose the
documentation engine that best suits your needs. SciCookie offers you four
documentation engine options for your Python package: _mkdocs_, _sphinx-rst_,
_sphinx-myst_, _jupyter-book_ and _quarto_. Additionally styling options
(themes) are provided for your documentation.

- [**mkdocs**](https://www.mkdocs.org/): is a fast, simple, and downright
  gorgeous static site generator for creating project documentation.
  Documentation source files are written in _Markdown_ and configured with a
  single `YAML` configuration file. It is designed to allow users to quickly
  create clear and well-structured documentation without requiring advanced
  programming skills. _mkdocs_ can be easily integrated with version control
  systems such as Git, supports a variety of predefined themes that allow you to
  customise the visual appearance of your documentation. In SciCookie you can
  choose between the
  [MkDocs (default)](https://www.mkdocs.org/user-guide/choosing-your-theme/#mkdocs),
  [Material](https://github.com/squidfunk/mkdocs-material),
  [Cinder](https://github.com/chrissimpkins/cinder) and
  [readthedocs](https://www.mkdocs.org/user-guide/choosing-your-theme/#readthedocs)
  themes.

- [**Sphinx**](https://www.sphinx-doc.org/en/master/): _Sphinx_ makes it easy to
  create intelligent and attractive documentation. It provides various output
  formats such as HTML, LaTeX, ePub, Texinfo, manual pages, plain text. It
  allows the use of built-in extensions for automatic code snippet checking, the
  inclusion of docstrings from Python modules, and third-party extensions to
  include many more features. To work with _Sphinx_ you can select either of the
  two available options: _sphinx-rst_ and _sphinx-myst_. _Sphinx-rst_ uses the
  _reStructuredText_ markup language by default and _Sphinx-myst_(Markedly
  Structured Text - Parser) is a Sphinx and Docutils extension to parse MyST, a
  rich and extensible flavour of Markdown for authoring technical and scientific
  documentation. Also, SciCookie offers themes to customize the look and feel of
  your documentation : a clean and minimalist theme (default -
  [Alabaster](https://sphinx-themes.org/sample-sites/default-alabaster/)), one
  that is very popular among scientists for its documentation –
  [Read the Docs](https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/) and
  another collection of themes for
  [PyData](https://sphinx-themes.org/sample-sites/pydata-sphinx-theme/) made for
  a particular kind of data science projects.

- [**Jupyter Book**](https://jupyterbook.org/en/stable/intro.html): allows you
  to create engaging, publication-quality books and documents from computational
  content. _Jupyter Book_ uses Jupyter notebooks as the basis for creating
  interactive content. It allows you to structure and organise the notebooks
  into a cohesive, navigable book. It also offers customisation options to adapt
  the look and feel of the book to your needs and extensions to add additional
  features. It can generate books in a variety of output formats, including
  HTML, PDF and static web pages. It integrates well with version control
  systems such as Git. If you want to customise the look or style of the
  documentation, SciCookie lets you choose between the default
  ([Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/)) theme or one
  derived from sphinx such as
  [Readthedocs](https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/) or
  [PyData](https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/index.html).

- [**Quarto**](https://quarto.org/): It is a versatile open-source platform
  designed for scientific and technical publishing. It offers the unique feature
  of embedding Python code directly into your documentation, enabling
  interactive and dynamic content creation. With Quarto, you can easily render
  your documents in multiple formats such as HTML, PDF, and websites, making it
  convenient for sharing and presenting your work. In addition, Quarto offers
  customisation options to personalise your content according to your
  preferences and needs. Through SciCookie, you can choose from some of the
  themes available in Quarto: [Default](https://bootswatch.com/default/),
  [Cosmo](https://bootswatch.com/cosmo/),
  [Cerulean](https://bootswatch.com/cerulean/),
  [Materia](https://bootswatch.com/materia/).

If you think we should add more options of documentation engines or themes, you
can submit your suggestion as a issue at
https://github.com/osl-incubator/scicookie/issues/new/choose.

## Project tools

SciCookie allows you to choose between several tools that can improve your
project in different ways. Some of these tools can help you automate tasks,
others allow you to format your code consistently, and others can help you find
errors and vulnerabilities in your code, and much more.

The tools are described below according to their functionality.

### Virtual environment

When working with Python, you should always have a virtual environment. This is
an isolated space where you can install and run applications and software
packages independently, without interfering with other environments or versions
on your system. You control which package versions are installed and when they
are updated. Virtual environments are disposable; you can delete and create as
many as you like. In Python there are many tools to manage virtual environments,
in SciCookie we offer you the option to use _conda_ as your environment
management system, which is a very popular option in the Python scientific
community.

- [**Conda**](https://docs.conda.io/en/latest/): is an open source package and
  environment management system that runs on Windows, MacOS and Linux. It
  quickly installs, runs and updates packages and their dependencies. It also
  makes it easy to create, save, load and switch between environments on your
  local machine, which is why we use conda as an option in SciCookie. If you
  want an easy way to choose a specific version of Python, and if your project
  relies on complex software libraries that are not easily installed with pip,
  using conda is a good option. It is included in all versions of Anaconda and
  Miniconda.

  If you select this option, a conda folder will appear in the project
  directory, containing a dev.yaml file that you can use to manage the
  development project's dependencies. If you do not select this option, a
  requirements.txt will be added for you to manage with virtualenv.

### Code formatter

A code formatter is a tool that automatically reformats code to conform to a set
of coding standards, such as PEP 8 guidelines. It helps us ensure consistency in
our code, saves time by automating the formatting process, reduces errors by
enforcing coding standards, and facilitates collaboration by making it easier
for multiple developers to work on the same code base. In the options of
SciCookie, you will find: _Black_.

- [**Black**](https://black.readthedocs.io): It is a popular code formatter tool
  for Python that automatically formats code to conform to PEP 8 guidelines. It
  provides a simple and opinionated way to format code, making it easy to use.
  The advantages of using Black include its ability to ensure consistent
  formatting, save time by automating the process, and reduce errors by
  enforcing coding standards.

You can read the [_black documentation_](https://black.readthedocs.io) if you
want to know more about it.

- [**Ruff**](https://docs.astral.sh/ruff/): Ruff is a versatile tool for Python
  that offers both linting and auto-formatting capabilities. As an
  auto-formatter, Ruff ensures consistent code formatting, fixes import sorting,
  and adheres to best practices. Notably, Ruff is significantly faster than
  tools like Black, making it ideal for large codebases. Its benefits include
  enhancing code readability, saving time on manual formatting, and allowing for
  fine-tuned configurations to meet specific project needs.

Using code formatters such as _Black_ and _Ruff_ in your project helps ensure
consistent and readable code, making it easier to maintain and collaborate on.

### Code security vulnerabilities

The code security vulnerabilities are errors or weaknesses in code that can be
exploited by attackers to gain unauthorized access, steal data, or cause damage
to a system.

To verify and prevent these vulnerabilities, there are several tools available
in Python. One such tool available in SciCookie is _Bandit_.

- [**Bandit**](https://bandit.readthedocs.io): It is a tool specifically
  designed to identify security issues in Python code. It scans code for common
  security problems such as hard-coded passwords and insecure file permissions.
  Some of the key features of Bandit are its ease of use, its ability to
  integrate with other tools and support for multiple versions of Python. To
  learn more about Bandit, you can read its
  [documentation](https://bandit.readthedocs.io/en/latest/).

It is important to use code vulnerability detection tools because they can help
identify security vulnerabilities in software and fix them before they can be
exploited by attackers. This helps to ensure the security and reliability of the
project.

### Code coverage testing

Code coverage testing is a software testing method that measures the percentage
of code that is executed during a test run. This can be used to identify areas
of code that are not being tested and to improve the overall quality of the
software.

There are a number of different code coverage tools available in Python. In
SciCookie you have _coverage_ available.

- [**Coverage**](https://coverage.readthedocs.io/): It is an open source tool
  for measuring the code coverage of a program. This means that it measures what
  percentage of the program code was executed when the tests were run. Coverage
  can be useful for identifying parts of the code that are not being tested and
  may be vulnerable to bugs. This will show you the percentage of code covered
  by your tests, as well as detailed information about which lines were executed
  and which were not. If you want to know more about how it works, you can read
  the [Coverge documentation](https://coverage.readthedocs.io/).

By using code coverage testing in Python, you can ensure that your code has been
thoroughly tested and is free of bugs.

### Code style and logic (code quality)

Code style refers to the way in which your code is written. It includes things
like indentation, line breaks, and variable names. Code logic refers to the way
in which your code works. It includes things like the flow of your code, the use
of data structures, and the implementation of algorithms.

There are a number of tools that can help you to improve the code style and
logic of your Python code; analyzing and verification of the code. In SciCookie
you can choose and include in your project _flake8_, _Ruff_, _isort_, _mccabe_,
_pydocstyle_ and/or _vulture_.

- [**Flake8**](https://flake8.pycqa.org/): A tool that helps you find potential
  performance issues in your code. Flake8 can detect errors in syntax,
  indentation, naming conventions, and other types of style errors. It can be
  useful for improving the quality of Python code. Flake8 enforces coding style
  conventions defined in the Python Enhancement Proposal 8 (PEP 8).
  Additionally, flake8 integrates well with popular code editors like Visual
  Studio Code, PyCharm, and Sublime Text. It can highlight style violations
  directly in your editor, making it easy to spot and fix issues as you write
  code. Flake8 can also be integrated into continuous integration and deployment
  (CI/CD) pipelines to ensure code quality standards are met before merging
  changes.

- [**Ruff**](https://beta.ruff.rs/docs/): This is an extremely fast Python
  linter written in Rust. Linting is the process of inspect code for potential
  bugs or style issues, and Ruff is designed to perform this analysis quickly
  and efficiently. It is particularly useful for large codebases where
  traditional Python linters can be slow and resource intensive.

  Ruff is designed to be easy to use and can be integrated into existing Python
  development workflows. It can be used as a standalone command line tool, or
  integrated into editors and IDEs using plugins or extensions. It is also able
  to detect a wide range of potential errors and style issues, and provides
  clear and detailed error messages to help developers resolve these issues
  quickly.

- [**isort**](https://pycqa.github.io/isort/): is a Python utility/library for
  automatically sorting imports alphabetically and separating them into sections
  and by type. This can help maintain a consistent import style and make the
  code easier to read. _isort_ provides a command-line utility, a Python library
  and plugins for various editors to quickly sort all your imports. It offers a
  number of configuration options to suit each project's import style
  preferences, has official pre-commit support and is black-compatible.

- [**McCabe**](https://here-be-pythons.readthedocs.io/en/latest/python/mccabe.html):
  is a code complexity checker that automatically detects code complexity based
  on cyclomatic complexity, which is roughly equal to one plus the number of
  loops and if statements. Simply put, it provides an upper bound on the number
  of test cases needed to obtain branch coverage of the code. It is recommended
  to run it during the git hook pre-commit.

- [**Vulture**](https://github.com/jendrikseipp/vulture): finds unused code in
  Python programs. This is useful for cleaning up and finding bugs in large code
  bases. Due to the dynamic nature of Python, static code analysers such as
  _Vulture_ are likely to miss some dead code. However, it can be a very useful
  tool for improving code quality. It uses static code analysis, it is
  self-testing and has full test coverage, it complements pyflakes and has the
  same output syntax, it sorts classes and functions by size and it supports
  Python >= 3.6, these are some of the main features of _Vulture_.

- [**pydocstyle**](http://www.pydocstyle.org/en/stable/): is a static analysis
  tool for checking compliance with Python docstring conventions. _pydocstyle_
  analyses source code for docstrings and verifies that they comply with the
  guidelines set out in PEP 257. This includes rules such as the formatting of
  docstrings, the presence of required sections, and the appropriate use of
  punctuation and structure. _pydocstyle_ supports Python 3.7 to 3.11 and can be
  integrated into development workflows as part of code review or automated
  validation processes.

When writing your code, you should always try to make it as clear and concise as
possible. This will make it easier for other developers to understand your code
and make changes if necessary. It is also important to use data structures and
algorithms that are appropriate for the task at hand. This will help ensure that
your code is efficient and scalable.

### Testing framework

A test framework is a software tool that provides a set of guidelines,
conventions, and utilities for writing and executing automated tests. It
provides a structure for organizing tests, and typically includes features for
test discovery, test execution, and test reporting.

Test frameworks help to ensure the quality of software by automating the testing
process. They allow developers to write tests that can be easily executed and
repeated, and provide feedback on the success or failure of the tests. There are
several options available for developing Python packages. SciCookie supports
_pytest_ and _hypothesis_.

- [**Pytest**](https://docs.pytest.org/en/): It is a popular testing framework
  for Python. It simplifies the process of writing and running tests by
  providing a concise syntax and powerful features. With Pytest, you can
  automatically discover and collect test cases, use fixtures for test setup and
  resource management, and write test functions with assert statements to check
  expected outcomes. It offers various options for test execution, including
  running specific tests, parallel execution, and generating test reports.
  Pytest also has a thriving ecosystem of plugins that extend its capabilities,
  such as code coverage analysis and test parameterization. Overall, Pytest is
  widely adopted for its simplicity, flexibility, and community support, making
  it an effective tool for ensuring the quality and reliability of Python code.
  You can know more about it in its
  [documentation](https://docs.pytest.org/en/).

- [**Hypothesis**](https://hypothesis.readthedocs.io/): is a property-based
  testing library for Python. It focuses on generating diverse input data and
  exploring different scenarios to thoroughly test code. Instead of relying on
  specific examples, Hypothesis allows you to define general properties that
  your code should satisfy. It automatically generates random inputs, including
  edge cases, to uncover potential bugs and unexpected behaviors. Hypothesis
  integrates well with popular testing frameworks like Pytest and promotes
  comprehensive testing to improve code reliability. If you want to know more,
  check out the documentation [here](https://hypothesis.readthedocs.io/).

### Static analysis of shell scripts

This is the process of analyzing the code of a shell script without actually
executing it. This is done by using specialized software tools that can scan the
script and identify potential issues such as syntax errors, coding standards
violations, security vulnerabilities, and performance problems. In SciCookie you
have _ShellCheck_ available.

- [**ShellCheck**](https://github.com/koalaman/shellcheck): This is a static
  analysis tool for shell scripts. It checks shell scripts for common errors and
  potential bugs, such as syntax errors, variable misuse, and command
  substitution issues. Shellcheck supports various shells, including Bash, Dash,
  and Zsh, and it can be integrated into various text editors and IDEs. Some
  advantages of using Shellcheck may include its ability to catch potential bugs
  before they cause issues, its support for multiple shells, and its ease of
  integration with various development environments. For more information, you
  can visit its [website](https://www.shellcheck.net/) or its repository on
  [GitHub](https://github.com/koalaman/shellcheck.net).

The static analysis of shell scripts is an important tool in your project, it
ensure that your code is of high quality, secure, and efficient.

Each tool has its own purpose and can be useful in different situations. When
choosing among these tools, it's important to consider your specific needs and
which tools may be most useful for your project.

### Pre-commit verification

It is a code quality control tool that runs automatically before commits are
made to a version control repository. When a commit is made, pre-commit executes
the configured hooks. If you select the pre-commit option offered by SciCookie,
we have configured the following hooks for you: _end-of-file-fixer_, _black_,
_flake8_, _ruff_, _isort_, _mypy_, _shellcheck_, _bandit_, _pydocstyle_,
_vulture_, _mccabe_ and _prettier_ (will be available in your project according
to the tools you have selected in TUI).

- [**pre-commit**](https://pre-commit.com/): It is a framework for managing and
  maintaining multi-language pre-commit hooks. A list of desired hooks must be
  specified, and pre-commit manages the installation and execution of all hooks
  written in any language before each commit. You will be notified before the
  end of the commit if validation fails, as configured.

This is configured using a `.pre-commit-config.yaml` file in the repository,
which sets the hooks to be executed before each commit. You can check the
supported hooks using this link https://pre-commit.com/hooks.html.

## Integration with DevOps tools

Integrating your Python project with DevOps tools can bring a number of benefits
to the development and deployment process. DevOps tools are designed to automate
and streamline the development pipeline, from code development to deployment and
maintenance, and can help you improve the speed, quality and reliability of the
development process. In SciCookie you can choose between _Docker_, _Podman_ and
_Kubernetes_. These are all containerization technologies used to deploy and
manage applications.

- [**Docker**](https://www.docker.com/): This is a containerization platform
  that allows developers to package their applications and dependencies into a
  portable container. Containers are lightweight, efficient, and provide a
  consistent runtime environment, making it easier to deploy and run
  applications across different environments. In Python projects, Docker can be
  used to package and deploy Python applications and dependencies, providing a
  consistent runtime environment and making it easier to manage dependencies and
  configurations. You can read more about this on the
  [Docker website](https://www.docker.com/) and in the
  [Docker documentation](https://docs.docker.com/).

- [**Podman**](https://podman.io/): It is a container engine without the need
  for a daemon running as root. With Podman, you can easily create and run
  containers, as well as manage their lifecycle and resources. This integration
  improves development and deployment processes, making them more efficient and
  streamlined. Podman in Python project helps to achieve a more secure,
  efficient and flexible containerization strategy and gives more control over
  application dependencies and configurations. As Podman allows containers to be
  managed without the need for a daemon, it provides a more secure and
  lightweight solution. You can read more about this on the
  [Podman website](https://podman.io/) and in the
  [Podman documentation](https://docs.podman.io/).

- [**Kubernetes**](https://kubernetes.io/): It is a container orchestration
  platform that automates the deployment, scaling, and management of
  containerized applications. It provides a platform for managing and scaling
  containerized applications across multiple hosts and environments, and offers
  advanced features such as automatic scaling, rolling updates, and
  self-healing. In Python projects, Kubernetes can be used to manage and
  orchestrate containerized Python applications, providing a scalable and
  reliable platform for running and deploying applications. You can read more
  about this on the [Kubernetes website](https://kubernetes.io/) and in the
  [Kubernetes documentation](https://kubernetes.io/docs/).

Overall, Docker, Podman, and Kubernetes are powerful tools for managing and
deploying containerized applications, and can provide a streamlined and
efficient platform for running Python projects.

In case you do not want to include DevOps in your project, you can do so by
selecting the option `None` (this is the default option).

## Automation tools

An automation tool is software or a platform designed to automate repetitive
tasks, processes, or workflows that are traditionally performed manually. These
tools are used to streamline and optimize various operations, reduce human
intervention, increase efficiency, and minimize errors. Currently, SciCookie
allows you to use `Make` and/or `Makim`.

- [Makim](https://osl-incubator.github.io/makim): Makim is an innovative tool
  inspired by make, designed to simplify target and dependency definition
  through YAML format. It introduces advanced features such as conditionals,
  arguments, and dependencies with targeted parameters. It also facilitates
  organized grouping of targets and supports user-defined variables and
  environment variables. Makim empowers users to streamline documentation and
  parameterize targets effectively. This free and open-source tool offers
  improved target management while maintaining compatibility with familiar YAML
  syntax.

- [Make](<https://en.wikipedia.org/wiki/Make_(software)>): Make is a versatile
  build automation tool that uses Makefiles to define rules and dependencies for
  compiling code and building projects. It automates the process, intelligently
  rebuilding only changed components, streamlining software development
  workflows.

## Project team

The project team refers to the group of people responsible for developing and
maintaining the project. This includes developers, designers, testers and other
stakeholders involved in the project. It is important that they are governed by
some rules and regulations so that they become a friendly group with standards
that others can follow and form a wider community. In SciCookie, we have some
options that are linked to the _code of conduct_, the _governance document_ and
the _roadmap_.

### Code of conduct

A code of conduct is a set of guidelines that outlines the expected behavior of
individuals participating in a community or organization. It typically specifies
the types of behavior that are considered acceptable and unacceptable, as well
as the consequences for violating the code of conduct. In SciCookie you can find
and choose between three adaptations of well-known codes of conduct accepted by
a large part of the community: _A Code of Conduct for Open Source Communities by
Contributors Covenant_,_The Citizen Code of Conduct_,and an adapted version of
the NumFOCUS and Python Codes of Conduct.

- **`contributor-covenant` option**: The Contributor Covenant aims to create a
  safe and inclusive environment for all contributors to open source projects.
  By promoting inclusive language, respectful communication, and a
  zero-tolerance policy for harassment and discrimination, it helps to ensure
  that everyone can participate in open source communities without fear of
  discrimination or mistreatment. If you want to know more about this, you can
  visit the full text of this
  [code of conduct](https://www.contributor-covenant.org/).

- **`citizen-code-of-conduct` option**: The Citizen Code of Conduct is intended
  to create a safe and welcoming environment for all members of the community.
  By promoting respectful communication, inclusive behavior, and collaboration,
  it helps to ensure that everyone can participate in the community without fear
  of discrimination or mistreatment. If you would like to know more, you can
  read the full text of this
  [code of conduct](https://github.com/stumpsyn/policies/blob/7caa4699ba74e341a46b3266d4610af477ba2c3d/citizen_code_of_conduct.md#citizen-code-of-conduct).

- **`numfocus-adapted-coc` option**: It is an adaptation of the NumFocus Code of
  Conduct, promotes kindness, respect, professionalism, good communication,
  among others. It does not tolerate harassment, regardless of gender, sexual
  orientation, gender identity and expression, disability, physical appearance,
  body size, race or religion of the members; nor sexist, racist or exclusionary
  jokes. If you wish to read the full text, please visit this link
  [code of conduct](https://numfocus.org/code-of-conduct)

- **`python-adapted-coc` option**: This option is an adaptation of the Python
  Code of Conduct prioritizing inclusivity, respect, and a welcoming community.
  It emphasizes kindness, discourages discrimination, and encourages positive
  contributions, consideration, and collaboration among all members. If you
  would like to know more, you can read the full text of this
  [code of conduct](https://www.python.org/psf/conduct/).

In case you do not want to include this file in your project, you can do so by
selecting the option `None` (this is the default option).

### Governance document

A governance document is a formal document that outlines the structure,
policies, and procedures of an organization or community. It typically describes
how decisions are made, how resources are allocated, and how conflicts are
resolved. This can take many different forms, depending on the needs and goals
of the organization or community. SciCookie offers two adaptations for your
project governance document: _NumPy Governance_ and _SciML Scientific Machine
Learning Governance_.

- **`numpy-governance` option**: NumPy is a widely used open source project for
  scientific computing in Python. Its governance document outlines how the
  project is managed and how decisions are made.
  [_The NumPy governance document_](https://numpy.org/doc/stable/dev/governance/index.html)
  describes the roles and responsibilities of the project's contributors,
  maintainers, and steering council, as well as the decision-making processes
  and procedures for contributing to the project. It emphasizes the importance
  of transparency, inclusivity, and participation in the development of the
  project. The **NumPy Governance Document** provides a clear framework for the
  management of the project and helps to ensure that it remains a vibrant and
  sustainable community-driven project. If you want to read the full text of
  Numpy's governance document, click
  [here](https://numpy.org/doc/stable/dev/governance/index.html).

- **`sciml-governance` option**:
  [_SciML Scientific Machine Learning Governance_](https://sciml.ai/governance/)
  is a governance document that outlines the structure and decision-making
  processes of the SciML community, which focuses on the development of
  scientific machine learning tools and methods. The document describes the
  roles and responsibilities of community members, including the Steering
  Committee and Technical Leaders. It also outlines the community's
  decision-making processes, including how new projects are proposed and
  accepted, and how conflicts and disputes are handled. The governance document
  emphasizes the importance of collaboration, inclusivity and transparency in
  the development of scientific machine learning tools and methods. It also
  provides a clear framework for the governance of the community, helping to
  ensure that it remains a vibrant and effective force in the development of
  scientific machine learning. If you want to read the full text of SciML
  Scientific Machine Learning Governance, click
  [here](https://sciml.ai/governance/).

In case you do not want to include this file in your project, you can do so by
selecting the option `None` (this is the default option).

### Roadmap document

A roadmap is a strategic plan that outlines the objectives, milestones and
actions required to achieve a specific goal or vision. It is typically used in
business, project management and product development to provide a high-level
overview of the steps required to achieve a desired outcome. A roadmap can
include timelines, budgets, resource requirements and key performance indicators
to track progress and measure success. The purpose is to provide a clear and
actionable plan for achieving a goal and to communicate that plan to
stakeholders and team members. SciCookie offers an adaptation for your project
roadmap document: _PyTorch-Ignite roadmap_.

- **`pytorch-ignite-roadmap` option**: PyTorch Ignite is an open-source library
  for high-level training and evaluation of neural networks in PyTorch. The
  PyTorch Ignite roadmap outlines the development plans for the library,
  including new features, bug fixes, and performance improvements. The roadmap
  may include timelines for releasing new versions, as well as details on
  specific features that are planned for each release. If you want to read the
  full text of PyTorch Ignite Roadmap, click
  [here](https://github.com/pytorch/ignite/wiki/Roadmap).

In case you do not want to include this file in your project, you can do so by
selecting the option `None` (this is the default option).

## Version control

Version control is essential for any project because it enables us to track and
store all versions and changes made to our codebase. With this in mind, we have
added some functionalities to SciCookie that allow you to easily add your Git
account information and project URLs.

By filling in the following fields, you can integrate your codebase with Git and
take advantage of its powerful version control features:

**git_username**: This is where you can enter your Git username, which will be
used only in the text of the documentation.

**git_https_origin**: This is the Git https origin URL, which is used for
configuring your repository in your local environment.

**git_https_upstream**: This is the Git https upstream URL, which is used for
adding on text of documentation installation and the contributing file, as well
as configuring your repository in your local environment.

**git_main_branch**: This field allows you to specify the name of your main
branch. By default, it is named "main".

By providing this information, you can easily integrate your codebase with
GitHub and take advantage of its powerful version control features. These
functionalities in SciCookie make it easy to manage your project and collaborate
with others, while ensuring that your code is properly versioned and tracked.
