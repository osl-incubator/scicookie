# tests/smoke/sphinx.sh

rm -rf /tmp/osl-python-package
cookiecutter --output-dir /tmp/ --no-input . documentation_engine=sphinx
cd /tmp/osl-python-package
mamba env create --file conda/dev.yaml --force
conda init bash
. ~/.bashrc
conda activate osl-python-package
poetry install
pre-commit install
make lint
make docs
make build
