# ref: https://github.com/mamba-org/micromamba-docker/blob/main/Dockerfile
{% if cookiecutter.add_containers == "Docker" %}
FROM condaforge/mambaforge:latest
{% else %}
FROM docker.io/condaforge/mambaforge:latest
{% endif %}
LABEL maintainer="{{ cookiecutter.author_full_name }} <{{ cookiecutter.author_email }}>"
LABEL org.opencontainers.image.title="{{ cookiecutter.project_name }}"
LABEL org.opencontainers.image.authors="{{ cookiecutter.project_name }} Team"
LABEL org.opencontainers.image.source="{{ cookiecutter.git_https_origin }}"
LABEL org.opencontainers.image.version="latest"
LABEL org.opencontainers.image.description="{{ cookiecutter.project_short_description }}"

# it is the default, but using it here to have it explicitly
USER root

{% if cookiecutter.add_containers == "Docker" -%}
SHELL ["/bin/bash", "-c"]
{%+ endif -%}
# Use bash in Dockerfile RUN commands and make sure bashrc is sourced when
# executing commands with /bin/bash -c
# Needed to have the micromamba activate command configured etc.

ENV ENV_NAME={{ cookiecutter.package_slug }}
{% if cookiecutter.add_containers == "Docker" -%}
ENV DEBIAN_FRONTEND=noninteractive
{% endif -%}
ARG UID=1000
ARG GID=1000

{% if cookiecutter.add_containers == "Docker" -%}
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
{% else %}
RUN dnf update -y && \
    dnf install -y --nodocs \
{% endif -%}
        build-essential \
        curl \
        git \
        libffi-dev \
        libldap2-dev \
{% if cookiecutter.add_containers == "Docker" -%}
        libpq-dev \
{% endif -%}
        libsasl2-dev \
        libssl-dev \
        locales \
{% if cookiecutter.add_containers == "Docker" -%}
        postgresql-client \
{% else %}
        postgresql
{% endif -%}
        vim && \
    rm -rf /var/lib/apt/lists/*

USER {{ cookiecutter.package_slug }}

WORKDIR /{{ cookiecutter.project_slug }}

COPY pyproject.toml .

# Create and copy virtual environment: Poetry is configured not to create a new
# virtual environment and necessary dependencies are installed without
# development packages

RUN mamba install -y poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi


COPY . /{{ cookiecutter.project_slug }}/

COPY . .

COPY compose.yaml .
{% if cookiecutter.add_containers == "Docker" %}
CMD ["python", "{{ cookiecutter.package_slug }}.py"]
{% else %}
CMD ["micromamba", "run", "-n", "{{ cookiecutter.package_slug }}", "python", "{{ cookiecutter.package_slug }}.py"]
{% endif %}
