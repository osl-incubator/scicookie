#!/usr/bin/env bash
echo "-------------------- Smoke test for ${1} -------------------"
set -ex

PATH_ORI=${PATH}
PWD_ORI=$(pwd)
PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" && cd ../src/scicookie && pwd )" >/dev/null 2>&1 && cd ../.. && pwd )"

if [ "$(which conda)}" == ""]; then
  echo "INVALID 'CONDA_PATH' environment variable."
  exit 1
fi

ENV_NAME=osl-python-package

OUTPUT_DIR="/tmp/osl"
rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

cookieninja --no-input \
  --output-dir "${OUTPUT_DIR}" \
  "${PROJECT_PATH}/src/scicookie" \
  ${1}

cd "${OUTPUT_DIR}/${ENV_NAME}"

eval "$(conda shell.bash hook)"
mamba env create --file conda/dev.yaml --force
conda activate "${ENV_NAME}"

# remove any path to scicookie environment
export PATH=$(echo $PATH| sed -E "s/[^:]+\/scicookie\/[^:]+//g")

if command -v poetry &> /dev/null; then
  poetry install
elif command -v flit &> /dev/null; then
  flit install
elif command -v meson &> /dev/null; then
  pip install .
elif command -v pdm &> /dev/null; then
  pdm install
elif command -v hatch &> /dev/null; then
  pip install .
elif command -v maturin &> /dev/null; then
  pip install .
elif [ "$(pip list|grep -c scikit_build_core)" -ne "0" ]; then
  pip install .
elif [ "$(pip list|grep -c pybind11)" -ne "0" ]; then
  # Assuming you are inside the root of the CMake source directory
  pip install .
else
  # use setuptools
  pip install .
fi

ipython kernel install --name "python3" --user

if command -v makim &> /dev/null; then
  makim tests.linter
  makim docs.build
  makim package.build
elif command -v make &> /dev/null; then
  make lint
  make docs-build
  make build
else
  echo "Makim and Make were not found in the system."
  exit 1
fi

export PATH=${PATH_ORI}

echo '---------------------------- passed --------------------------'
cd "${PWD_ORI}"
