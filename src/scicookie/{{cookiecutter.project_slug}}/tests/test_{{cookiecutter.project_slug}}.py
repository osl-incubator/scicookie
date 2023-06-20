"""Tests for `{{ cookiecutter.project_slug }}` package."""
{%- if cookiecutter.use_pytest == "yes" -%}

import pytest


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
{% endif %}

{%- if cookiecutter.use_hypothesis == "yes" -%}

from hypothesis import given, strategies as st 

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: https://hypothesis.readthedocs.io/en/latest/quickstart.html
    """


@given(st.text())
def test_content(response, hypothesis_argument):
    """Sample pytest test function with the pytest fixture and hypothesis as arguments."""
    # Test code using the response fixture and hypothesis_argument
{% endif %}
