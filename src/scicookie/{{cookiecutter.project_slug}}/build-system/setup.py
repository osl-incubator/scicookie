# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup


setup(
    name="OSL Python package",
    author="{{cookiecutter.author_full_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://{{ cookiecutter.project_slug }}.com",
    description="A test project using pybind11",
    long_description="",
    #extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    python_requires=">=3.7",
)
