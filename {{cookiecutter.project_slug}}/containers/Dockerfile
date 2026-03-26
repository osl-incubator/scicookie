# ref: https://github.com/mamba-org/micromamba-docker/blob/main/Dockerfile
{% if cookiecutter.use_containers == "Docker" %}
FROM condaforge/mambaforge:latest
{% elif cookiecutter.use_containers == "Podman" %}
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

SHELL ["/bin/bash", "-c"]

# Use bash in Dockerfile RUN commands and make sure bashrc is sourced when
# executing commands with /bin/bash -c
# Needed to have the micromamba activate command configured etc.

ENV ENV_NAME={{ cookiecutter.package_slug }}
ENV DEBIAN_FRONTEND=noninteractive
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        curl \
        git \
        libffi-dev \
        libldap2-dev \
        libpq-dev \
        libsasl2-dev \
        libssl-dev \
        locales \
        postgresql-client \
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

CMD ["python", "{{ cookiecutter.package_slug }}.py"]
