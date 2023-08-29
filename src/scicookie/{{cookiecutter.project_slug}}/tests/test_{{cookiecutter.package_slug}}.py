"""Tests for {{ cookiecutter.package_slug }} package."""
{% if cookiecutter.use_pytest == "yes" -%}
import pytest
{% endif -%}

{%- if cookiecutter.use_pytest == "yes" and cookiecutter.use_hypothesis == "yes" -%}
{# keep this line here #}
{# keep this line here #}
{%- endif -%}

{% if cookiecutter.use_hypothesis == "yes" -%}
from hypothesis import given
from hypothesis import strategies as st
{% endif -%}

{% if cookiecutter.use_pytest == "yes" %}

@pytest.fixture
def response_pytest():
    """Sample pytest fixture."""
    return True
{%- if cookiecutter.use_hypothesis == "yes" %}


@pytest.fixture
def response_hypothesis():
    """Sample pytest + hypothesis fixture."""
    return True
{%- endif -%}
{%- endif -%}

{%- if cookiecutter.use_pytest == "yes" %}


def test_content_pytest():
    """Test with pytest."""
    assert True
{%- if cookiecutter.use_hypothesis == "yes" %}


@given(st.text())
def test_content_hypothesis(response_hypothesis):
    """Test with pytest + hypothesis."""
    assert response_hypothesis
{%- endif -%}
{%- endif %}
{# keep this line at the end of the file -#}
