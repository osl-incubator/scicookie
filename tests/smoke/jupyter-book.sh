#!/usr/bin/env bash
echo '--------------- Smoke test for jupyter-book ------------------'
set -e

CONDA_PATH=$(cd $(dirname $(which conda)) && cd .. && pwd)

is_conda_in_path=$(echo $PATH|grep -m 1 --count ${CONDA_PATH})

if [ $is_conda_in_path == 0 ]; then
  export PATH="${CONDA_PATH}/condabin:${CONDA_PATH}/bin:$PATH"
  echo "[II] included conda to the PATH"
fi

rm -rf /tmp/osl-python-package

cookiecutter --output-dir /tmp/ --no-input . documentation_engine=jupyter-book
cd /tmp/osl-python-package

mamba env create --file conda/dev.yaml --force
${CONDA_PATH}/bin/activate osl-python-package

poetry install

pre-commit install
pre-commit run --all-files

make docs
make build

echo '---------------------------- passed --------------------------'
