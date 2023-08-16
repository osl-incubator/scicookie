#!/usr/bin/env bash
echo "-------------------- Smoke test for ${1} -------------------"
set -ex

PATH_ORI=${PATH}
PWD_ORI=$(pwd)
CONDA_PATH=$(cd "$(dirname ${CONDA_PYTHON_EXE})" && cd .. && pwd)
PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" && cd ../src/scicookie && pwd )" >/dev/null 2>&1 && cd ../.. && pwd )"

if [ "${CONDA_PATH}" == ""]; then
  echo "INVALID 'CONDA_PATH' environment variable."
  exit 1
fi

export PATH="${CONDA_PATH}/condabin:${CONDA_PATH}/bin:$PATH"
echo "[II] included conda to the PATH"

ENV_NAME=osl-python-package

OUTPUT_DIR="/tmp/osl"
rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

cookieninja --no-input \
  --output-dir "${OUTPUT_DIR}" \
  "${PROJECT_PATH}/src/scicookie" \
  ${1}

cd "${OUTPUT_DIR}/${ENV_NAME}"

mamba env create --file conda/dev.yaml --force

CONDA_PREFIX="${CONDA_PATH}/envs/${ENV_NAME}"

export PATH=$(echo $PATH| sed -E "s/[^:]+\/mambaforge\/[^:]+//g")
export PATH=$(echo $PATH| sed -E "s/[^:]+\/conda\/[^:]+//g")
export PATH=$(echo $PATH| sed -E "s/[^:]+\/miniconda\/[^:]+//g")
export PATH=$(echo $PATH| sed -E "s/[^:]+\/miniconda3\/[^:]+//g")
export PATH=$(echo $PATH| sed -E "s/[^:]+\/micromamba\/[^:]+//g")
export PATH=$(echo $PATH| sed -E "s/[^:]+\/anaconda3\/[^:]+//g")
export PATH="${CONDA_PREFIX}:${CONDA_PREFIX}/bin:$PATH"
echo "[II] included env conda to the PATH"
COMMAND_PREFIX=
if command -v poetry &> /dev/null; then
  poetry install
elif command -v flit &> /dev/null; then
  flit install
elif command -v meson &> /dev/null; then
  pip install .
elif command -v pdm &> /dev/null; then
  pdm install
elif command -v hatch &> /dev/null; then
  COMMAND_PREFIX="hatch run"
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

$COMMAND_PREFIX ipython kernel install --name "python3" --user

$COMMAND_PREFIX pre-commit install

$COMMAND_PREFIX pre-commit run --all-files --verbose

if command -v makim &> /dev/null; then
  $COMMAND_PREFIX makim docs.build
  makim build
else
  $COMMAND_PREFIX make docs-build 
  make build 
fi



export PATH=${PATH_ORI}

echo '---------------------------- passed --------------------------'
cd "${PWD_ORI}"
