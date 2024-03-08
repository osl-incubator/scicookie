# Installation

## Stable release

To install {{ cookiecutter.project_name }}, run this command in your terminal:

```bash
$ pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always
install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this
[Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/)
can guide you through the process.

## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from the [Github repo]({{ cookiecutter.git_https_upstream }}).

You can either clone the public repository:
{% if cookiecutter.git_https_upstream != "" %}
```bash
$ git clone {{ cookiecutter.git_https_upstream }}
```
{%- else %}
```bash
$ git clone https://github.com/MYORG/MYREPO
```
{%- endif %}

Or download the [tarball]({{ cookiecutter.git_https_upstream }}/tarball/main):

```bash
$ curl -OJL {{ cookiecutter.git_https_upstream }}/tarball/main
```

Once you have a copy of the source, you can install it with:

```bash
$ poetry install
```
