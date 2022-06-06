# tests/smoke/jupyter-book.sh

rm -rf /tmp/osl-python-package
cookiecutter --output-dir /tmp/ --no-input . documentation_engine=jupyter-book
cd /tmp/osl-python-package
mamba env create --file conda/dev.yaml --force
conda activate osl-python-package
poetry install
pre-commit install
pre-commit run --all-files
make docs
make build
