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

# note: keep it for history, we need to check if the current
#   approach would work anywhere, otherwise we need to revisit
#   this previous approach and maybe use sed to remove the previous
#   conda_prefix from the path.
#   CONDA_PREFIX="${CONDA_PATH}/envs/${ENV_NAME}"
#   export PATH="${CONDA_PREFIX}:${CONDA_PREFIX}/bin:$PATH"
source activate ${ENV_NAME}
echo "[II] included env conda to the PATH"

if command -v poetry &> /dev/null; then
  poetry install
elif command -v flit &> /dev/null; then
  flit install
fi

# ipython kernel install --name "python3" --user

pre-commit install
pre-commit run --all-files --verbose

make docs-build
make build

export PATH=${PATH_ORI}

echo '---------------------------- passed --------------------------'
cd "${PWD_ORI}"
