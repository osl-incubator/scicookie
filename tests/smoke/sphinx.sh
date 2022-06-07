#!/usr/bin/env bash
set -e
rm -rf /tmp/osl-python-package
cookiecutter --output-dir /tmp/ --no-input . documentation_engine=sphinx
cd /tmp/osl-python-package
mamba env create --file conda/dev.yaml --force
conda init bash
. ~/.bashrc
conda activate osl-python-package
poetry install
pre-commit install
pre-commit run --all-files
make docs
make build
