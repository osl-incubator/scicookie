#!/usr/bin/env bash
echo '--------------- Smoke test for jupyter-book ------------------'
set -e
rm -rf /tmp/osl-python-package
cookiecutter --output-dir /tmp/ --no-input . documentation_engine=jupyter-book
cd /tmp/osl-python-package
conda env create --file conda/dev.yaml --force
conda init bash
. ~/.bashrc
conda activate osl-python-package
poetry install
pre-commit install
pre-commit run --all-files
make docs
make build
echo '---------------------------- passed --------------------------'
