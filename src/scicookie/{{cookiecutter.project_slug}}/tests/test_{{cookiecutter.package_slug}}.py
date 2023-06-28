"""
Tests for {{ cookiecutter.package_slug }} package.
"""
{% if cookiecutter.use_pytest == "yes" -%}
import pytest
{% endif -%}
{% if cookiecutter.use_hypothesis == "yes" -%}
from hypothesis import given
from hypothesis import strategies as st
{% endif -%}
{% if cookiecutter.use_pytest == "yes" %}

@pytest.fixture
def response_pytest():
    """Sample pytest fixture.

    See more at:
    http://doc.pytest.org/en/latest/fixture.html
    """
{% endif -%}
{% if cookiecutter.use_hypothesis == "yes" %}

@pytest.fixture
def response_hypothesis():
    """Sample pytest fixture.

    See more at:
    https://hypothesis.readthedocs.io/en/latest/quickstart.html
    """
{% endif -%}

{%- if cookiecutter.use_pytest == "yes" and 
cookiecutter.use_hypothesis == "yes" %}

@given(st.text())
def test_content_hypothesis1():
    """Sample pytest test function with the
    pytest fixture and hypothesis as arguments.
    """
    # Test code using the response fixture and
    # hypothesis_argument


@given(st.text())
def test_content_hypothesis2():
    """Sample pytest test function with the hypothesis
    fixture as an argument.
    """
    # Test code using the response fixture and
    # hypothesis_argument
{% endif -%}
{#- keep this line at the end of the file -#}
