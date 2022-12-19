============
Installation
============

Stable release
~~~~~~~~~~~~~~

To install {{ cookiecutter.project_name }}, run this command in your
terminal:

.. sourcecode::

	$ pip install {{ cookiecutter.project_slug }}


This is the preferred method to install {{ cookiecutter.project_name }},
as it will always install the most recent stable release.

If you don't have `pip <https://pip.pypa.io>`_ installed, this
`Python installation guide <http://docs.python-guide.org/en/latest/starting/installation/>`_
can guide you through the process.

From sources
============

The sources for {{ cookiecutter.project_name }} can be downloaded from
the `Github repo <{{ cookiecutter.git_https_upstream }}>`_.

You can either clone the public repository:

.. sourcecode::

	$ git clone {{ cookiecutter.git_https_upstream }}


Or download the
`tarball <{{ cookiecutter.git_https_upstream }}/tarball/main>`_:

.. sourcecode::

	$ curl -OJL {{ cookiecutter.git_https_upstream }}/tarball/main

Once you have a copy of the source, you can install it with:

.. sourcecode::

	$ poetry install
