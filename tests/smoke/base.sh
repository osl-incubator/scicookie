#!/usr/bin/env bash
echo '-------------------- Smoke test for ${1} -------------------'
set -e

PATH_ORI=${PATH}
CONDA_PATH=$(cd $(dirname $(which conda)) && cd .. && pwd)
PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd ../.. && pwd )"

export PATH="${CONDA_PATH}/condabin:${CONDA_PATH}/bin:$PATH"
echo "[II] included conda to the PATH"

ENV_NAME=osl-python-package

rm -rf "/tmp/${ENV_NAME}"

cookiecutter --output-dir /tmp/ --no-input ${PROJECT_PATH} ${1}="${2}"
cd "/tmp/${ENV_NAME}"

mamba env create --file conda/dev.yaml --force

CONDA_PREFIX="${CONDA_PATH}/envs/${ENV_NAME}"
export PATH="${CONDA_PREFIX}:${CONDA_PREFIX}/bin:$PATH"
echo "[II] included env conda to the PATH"

poetry install

ipython kernel install --name "python3" --user

pre-commit install
pre-commit run --all-files

make docs-build
make build

export PATH=${PATH_ORI}

echo '---------------------------- passed --------------------------'
