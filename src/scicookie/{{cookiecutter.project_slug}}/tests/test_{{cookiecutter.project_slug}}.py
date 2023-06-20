"""Tests for `{{ cookiecutter.project_slug }}` package."""
{%- if cookiecutter.use_pytest == "yes" -%}
import pytest
{%- endif %}

{%- if cookiecutter.use_hypothesis == "yes" -%}
from hypothesis import given, strategies as st
{%- endif %}


{%- if cookiecutter.use_pytest == "yes" -%}
@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
{%- endif -%}


{%- if cookiecutter.use_hypothesis == "yes" -%}
@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: https://hypothesis.readthedocs.io/en/latest/quickstart.html
    """
{%- endif -%}


{%- if cookiecutter.use_pytest == "yes" and cookiecutter.use_hypothesis == "yes" -%}
@given(st.text())
def test_content(response, hypothesis_argument):
    """Sample pytest test function with the pytest fixture and hypothesis as arguments."""
    # Test code using the response fixture and hypothesis_argument

@given(st.text())
def test_content(response, hypothesis_argument):
    """Sample pytest test function with the hypothesis fixture as an argument."""
    # Test code using the response fixture and hypothesis_argument
{%- endif -%}
