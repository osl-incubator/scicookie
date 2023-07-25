# SciCookie user guide

SciCookie allows you to create a template for your Python project. The team has
created this guide to help you understand every option and its functionality.

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
    - [Virtual Environment](#virtual-environment)
    - [Code formatter](#code-formatter)
    - [Code Security Vulnerabilities](#code-security-vulnerabilities)
    - [Code coverage testing](#code-coverage-testing)
    - [Code style and logic (code quality)](#code-style-and-logic-code-quality)
    - [Testing framework](#testing-framework)
    - [Pre-commit verification](#pre-commit-verification)
    - [Static analysis of shell scripts](#static-analysis-of-shell-scripts)
  - [Integration with DevOps tools](#integration-with-devops-tools)
  - [Project team](#project-team)
    - [Code of conduct](#code-of-conduct)
    - [Governance document](#governance-document)
    - [Roadmap document](#roadmap-document)
  - [Control Version](#control-version)

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
   [ ] blue
   [ ] conda
   [ ] coverage
   [ ] flake8
   [ ] ruff
   [ ] isort
   [ ] mccabe
   [ ] pre-commit
   [ ] pydocstyle
   [ ] pytest
   [ ] hypothesis
```

Use the right arrow key to select the tools you want, and use the up and down
arrow keys to navigate through the list. If you accidentally select an option
you don't want, simply use the left arrow key to deselect it.

The following is a description of the options in the TUI.
## The author of project

- **author_name**
- **author_email**

## Information about the project

- project_name
- project_slug
- package_slug
<mencionar la diferencia entre project y package, muy importante>
- project_version
- project_url
- project_license

## Project settings

Setting up some configurations in the project structure is important because it
allows you to get an orderly workflow. With SciCookie you can configure elements
such as project layout, build system, command-line interface and documentation
engine. This can help streamline the development process by providing a
consistent and standardized framework for the project.

### Project layout

The organization of your code is important, which is why at SciCookie we offer
two alternatives: *src* and *flat*.

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

  Because all source files are on the same level in this layout, they are easy to
  find and access. However, as the project becomes larger and more complex, it can
  become more difficult to maintain and navigate the codebase.

  The flat structure is simpler and may be suitable for smaller projects or
  scripts where the codebase is relatively small and does not require extensive
  organization or separation of concerns.

Both **src** and **flat** layouts have their own advantages and disadvantages.
The choice between them depends on your specific requirements and the complexity
of your project, as well as your personal preferences and team conventions.

If you want to find more information about it you can visit:

- [Python Packaging User Guide » Discussions » src layout vs flat
  layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [The source
  layout](https://py-pkgs.org/04-package-structure.html#the-source-layout) in
  the book [Python Packages](https://py-pkgs.org/) by [Tomas
  Beuzen](https://www.tomasbeuzen.com/) & [Tiffany
  Timbers](https://www.tiffanytimbers.com/).
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
  few  commands, you can use Flit to quickly create source distributions and
  wheel packages and submit them to PyPI.

- [**meson-python**](https://meson-python.readthedocs.io/en/latest/index.html):
  It's a Python build backend built on top of the *Meson* build-system.
  It enables you to use Meson for your Python packages. With
  meson-python, you can easily define project dependencies, specify
  build options, generate configuration files and build scripts, among
  other things. Meson-python is primarily focused on improving speed and
  ease of use compared to other build systems. It is designed to be fast
  and scalable, making it suitable for both small and large projects.

- [**Setuptools**](https://setuptools.pypa.io/en/latest/): It's a package that
  facilitates the distribution and installation of Python packages. Setuptools
  provides a way to define metadata about your project, such as its name,
  version, dependencies, and other details. It also provides functionality for
  building and distributing packages, creating distribution archives, and
  installing packages with their dependencies.  *"It helps developers to easily
  share reusable code (in the form of a library) and programs (e.g., CLI/GUI
  tools implemented in Python), that can be installed with pip and uploaded to
  PyPI."*

- [**PDM**](https://pdm.fming.dev/): It's a modern Python package and
  dependency manager supporting the latest PEP standards. But it is more
  than a package manager. It boosts your development workflow in various
  aspects. It has very powerful features, including easy and fast
  dependency resolution, especially for large binary distributions, a
  PEP 517 compilation backend, PEP 621 project metadata, a flexible and
  powerful plugin system. It also offers, among other things, versatile
  user scripting, PyPI integration and version management.
  
- [**Hatch**](https://hatch.pypa.io): It's a PEP 517/PEP 660 compatible
  build backend used by Hatch, a modern, extensible Python project manager.
  It provides a standardized build system with reproducible builds by default,
  robust environment management with support for custom scripts, easy publishing
  to PyPI or other indexes, version management, and configurable project generation
  with sane defaults. Hatchling ensures that your builds are reproducible, so you
  can be confident that they will always produce the same results. It also helps
  you manage your Python environments, so you can be sure that your projects have
  the correct dependencies.
- [**Maturin**](https://pypi.org/project/maturin/0.8.2/):It's build system designed to create Python bindings from Rust projects. It allows Rust code to be seamlessly integrated into Python applications, providing efficient builds and cross-platform support for various Python versions. Maturin automates the generation of Python modules that directly access Rust functions, harnessing Rust's high performance and low-level capabilities within Python. Its user-friendly interface and compatibility with setuptools and Cargo make it an easy-to-use tool, offering developers a simple solution to combine the strengths of Python and Rust within a unified project.
The idea behind the options in SciCookie is that you can choose from some of the
most popular system compilers to suit your needs and preferences for developing
Python packages. If you think we should add more options, you can submit your
suggestion as a issue at
https://github.com/osl-incubator/scicookie/issues/new/choose.

### Command-line interfaces (CLIs)

- Click
- Argparse

### Documentation engine

- mkdocs
- sphinx
- jupyter-book

## Project tools

SciCookie allows you to choose between several tools that can improve your
project in different ways. Some of these tools can help you automate tasks,
others allow you to format your code consistently, and others can help you find
errors and vulnerabilities in your code, and much more.

The tools are described below according to their functionality.

### Virtual Environment

-**Conda**

### Code formatter

A code formatter is a tool that automatically reformats code to conform to a set
of coding standards, such as PEP 8 guidelines. It helps us ensure consistency in
our code, saves time by automating the formatting process, reduces errors by
enforcing coding standards, and facilitates collaboration by making it easier
for multiple developers to work on the same code base. In the options of
SciCookie, you will find two choices: Black and Blue.

- [**Black**](https://black.readthedocs.io): It is a popular code formatter tool
for Python that automatically formats code to conform to PEP 8 guidelines. It
provides a simple and opinionated way to format code, making it easy to use. The
advantages of using Black include its ability to ensure consistent formatting,
save time by automating the process, and reduce errors by enforcing coding
standards.

You can read the [*black documentation*](https://black.readthedocs.io) if you
want to know more about it.

- **Blue**

If you select both Blue and Black libraries in the TUI (Terminal User
Interface), you will see the following message: "The libs Blue and Black were
selected, but you need to choose just one of them." and the template generation
process will be stopped.

Using code formatters such as black or blue in your project helps ensure
consistent and readable code, making it easier to maintain and collaborate on.

### Code Security Vulnerabilities

The code security vulnerabilities are errors or weaknesses in code that can be
exploited by attackers to gain unauthorized access, steal data, or cause damage
to a system.

To verify and prevent these vulnerabilities, there are several tools available
in Python. One such tool available in SciCookie is *Bandit*.

- [**Bandit**](https://bandit.readthedocs.io): It is a tool specifically designed to
identify security issues in Python code. It scans code for common security
problems such as hard-coded passwords and insecure file permissions. Some of the
key features of Bandit are its ease of use, its ability to integrate with other
tools and support for multiple versions of Python. To learn more about Bandit,
you can read its [documentation](https://bandit.readthedocs.io/en/latest/).

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
SciCookie you have *coverage* available.

- [**Coverage**](https://coverage.readthedocs.io/): It is an open source tool
for measuring the code coverage of a program. This means that it measures what
percentage of the program code was executed when the tests were run. Coverage
can be useful for identifying parts of the code that are not being tested and
may be vulnerable to bugs. This will show you the percentage of code covered by
your tests, as well as detailed information about which lines were executed and
which were not. If you want to know more about how it works, you can read the
[Coverge documentation](https://coverage.readthedocs.io/).

By using code coverage testing in Python, you can ensure that your code has been
thoroughly tested and is free of bugs.

### Code style and logic (code quality)

Code style refers to the way in which your code is written. It includes things
like indentation, line breaks, and variable names. Code logic refers to the way
in which your code works. It includes things like the flow of your code, the use
of data structures, and the implementation of algorithms.

There are a number of tools that can help you to improve the code style and
logic of your Python code; analyzing and verification of the code. In SciCookie
you can choose and include in your project *flake8*, *Ruff*, *isort*, *mccabe*,
*pydocstyle* and/or *vulture*.

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
  integrated into editors and IDEs using plugins or extensions. It is also able to
  detect a wide range of potential errors and style issues, and provides clear and
  detailed error messages to help developers resolve these issues quickly.

- **Isort**
- **McCabe**
- **pydocstyle**
- **Vulture**

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
*pytest* and *hypothesis*.

- [**Pytest**](https://docs.pytest.org/en/): It is a popular testing framework
for Python. It simplifies the process of writing and running tests by providing
a concise syntax and powerful features. With Pytest, you can automatically
discover and collect test cases, use fixtures for test setup and resource
management, and write test functions with assert statements to check expected
outcomes. It offers various options for test execution, including running
specific tests, parallel execution, and generating test reports. Pytest also has
a thriving ecosystem of plugins that extend its capabilities, such as code
coverage analysis and test parameterization. Overall, Pytest is widely adopted
for its simplicity, flexibility, and community support, making it an effective
tool for ensuring the quality and reliability of Python code. You can know more
about it in its [documentation](https://docs.pytest.org/en/).

- [**Hypothesis**](https://hypothesis.readthedocs.io/): is a property-based
testing library for Python. It focuses on generating diverse input data and
exploring different scenarios to thoroughly test code. Instead of relying on
specific examples, Hypothesis allows you to define general properties that your
code should satisfy. It automatically generates random inputs, including edge
cases, to uncover potential bugs and unexpected behaviors. Hypothesis integrates
well with popular testing frameworks like Pytest and promotes comprehensive
testing to improve code reliability. f you want to know more, check out the
documentation [here](https://hypothesis.readthedocs.io/).

### Pre-commit verification

- **pre-commit**

### Static analysis of shell scripts

This is the process of analyzing the code of a shell script without actually
executing it. This is done by using specialized software tools that can scan the
script and identify potential issues such as syntax errors, coding standards
violations, security vulnerabilities, and performance problems. In SciCookie you
have *ShellCheck* available.

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

## Integration with DevOps tools

Integrating your Python project with DevOps tools can bring a number of benefits
to the development and deployment process. DevOps tools are designed to automate
and streamline the development pipeline, from code development to deployment and
maintenance, and can help you improve the speed, quality and reliability of the
development process. In SciCookie

- [**Docker**](https://www.docker.com/): This is a containerization platform
that allows developers to package their applications and dependencies into a
portable container. Containers are lightweight, efficient, and provide a
consistent runtime environment, making it easier to deploy and run applications
across different environments. In Python projects, Docker can be used to package
and deploy Python applications and dependencies, providing a consistent runtime
environment and making it easier to manage dependencies and configurations. You
can read more about this on the [Docker website](https://www.docker.com/) and in
the [Docker documentation](https://docs.docker.com/).

- [**Podman**](https://podman.io/): It is a container engine without the need
for a daemon running as root. With Podman, you can easily create and run
containers, as well as manage their lifecycle and resources. This integration
improves development and deployment processes, making them more efficient and
streamlined. Podman in Python project helps to achieve a more secure, efficient
and flexible containerization strategy and gives more control over application
dependencies and configurations. As Podman allows containers to be managed
without the need for a daemon, it provides a more secure and lightweight
solution. You can read more about this on the [Podman
website](https://podman.io/) and in the [Podman
documentation](https://docs.podman.io/).

- [**Kubernetes**](https://kubernetes.io/): It is a container orchestration
platform that automates the deployment, scaling, and management of containerized
applications. It provides a platform for managing and scaling containerized
applications across multiple hosts and environments, and offers advanced
features such as automatic scaling, rolling updates, and self-healing. In Python
projects, Kubernetes can be used to manage and orchestrate containerized Python
applications, providing a scalable and reliable platform for running and
deploying applications. You can read more about this on the [Kubernetes
website](https://kubernetes.io/) and in the [Kubernetes
documentation](https://kubernetes.io/docs/).

Overall, Docker, Podman, and Kubernetes are powerful tools for managing and
deploying containerized applications, and can provide a streamlined and
efficient platform for running Python projects.

## Project team

The project team refers to the group of people responsible for developing and
maintaining the project. This includes developers, designers, testers and other
stakeholders involved in the project. It is important that they are governed by
some rules and regulations so that they become a friendly group with standards
that others can follow and form a wider community. In SciCookie, we have some
options that are linked to the *code of conduct*, the *governance document* and
the *roadmap*.

### Code of conduct

A code of conduct is a set of guidelines that outlines the expected behavior of
individuals participating in a community or organization. It typically specifies
the types of behavior that are considered acceptable and unacceptable, as well
as the consequences for violating the code of conduct. In SciCookie you can find
and choose between two adaptations of well-known codes of conduct accepted by a
large part of the community, *A Code of Conduct for Open Source Communities by
Contributors Covenant* and *The Citizen Code of Conduct*.

- **`contributor-covenant` option**: The Contributor Covenant aims to create a
safe and inclusive environment for all contributors to open source projects. By
promoting inclusive language, respectful communication, and a zero-tolerance
policy for harassment and discrimination, it helps to ensure that everyone can
participate in open source communities without fear of discrimination or
mistreatment. If you want to know more about this, you can visit the full text
of this [code of conduct](https://www.contributor-covenant.org/).

- **`citizen-code-of-conduct` option**: The Citizen Code of Conduct is intended
to create a safe and welcoming environment for all members of the community. By
promoting respectful communication, inclusive behavior, and collaboration, it
helps to ensure that everyone can participate in the community without fear of
discrimination or mistreatment. If you would like to know more, you can read the
full text of this [code of
conduct](https://github.com/stumpsyn/policies/blob/7caa4699ba74e341a46b3266d4610af477ba2c3d/citizen_code_of_conduct.md#citizen-code-of-conduct).

In case you do not want to include this file in your project, you can do so by
selecting the option `None` (this is the default option).

### Governance document

A governance document is a formal document that outlines the structure,
policies, and procedures of an organization or community. It typically describes
how decisions are made, how resources are allocated, and how conflicts are
resolved. This can take many different forms, depending on the needs and goals
of the organization or community. SciCookie offers two adaptations for your
project governance document: *NumPy Governance* and *SciML Scientific Machine
Learning Governance*.

**numpy-governance** option: NumPy is a widely used open source project for
scientific computing in Python. Its governance document outlines how the project
is managed and how decisions are made. [*The NumPy governance
document*](https://numpy.org/doc/stable/dev/governance/index.html) describes the
roles and responsibilities of the project's contributors, maintainers, and
steering council, as well as the decision-making processes and procedures for
contributing to the project. It emphasizes the importance of transparency,
inclusivity, and participation in the development of the project. The **NumPy
Governance Document** provides a clear framework for the management of the
project and helps to ensure that it remains a vibrant and sustainable
community-driven project. If you want to read the full text of Numpy's
governance document, click
[here](https://numpy.org/doc/stable/dev/governance/index.html).

**sciml-governance** option: [*SciML Scientific Machine Learning
Governance*](https://sciml.ai/governance/) is a governance document that outlines
the structure and decision-making processes of the SciML community, which
focuses on the development of scientific machine learning tools and methods. The
document describes the roles and responsibilities of community members,
including the Steering Committee and Technical Leaders. It also outlines the
community's decision-making processes, including how new projects are proposed
and accepted, and how conflicts and disputes are handled. The governance
document emphasizes the importance of collaboration, inclusivity and
transparency in the development of scientific machine learning tools and
methods. It also provides a clear framework for the governance of the community,
helping to ensure that it remains a vibrant and effective force in the
development of scientific machine learning. If you want to read the full text of
SciML Scientific Machine Learning Governance, click
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
roadmap document, PyTorch-Ignite roadmap.


**pytorch-ignite-roadmap** option: PyTorch Ignite is an open-source library for
high-level training and evaluation of neural networks in PyTorch. The PyTorch
Ignite roadmap outlines the development plans for the library, including new
features, bug fixes, and performance improvements. The roadmap may include
timelines for releasing new versions, as well as details on specific features
that are planned for each release. If you want to read the full text of PyTorch
Ignite Roadmap, click [here](https://github.com/pytorch/ignite/wiki/Roadmap).

In case you do not want to include this file in your project, you can do so by
selecting the option `None` (this is the default option).

## Control Version

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
