#!/usr/bin/env bash
echo "-------------------- Smoke test for ${1} -------------------"
set -ex

PATH_ORI=${PATH}
PWD_ORI=$(pwd)
PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd ../.. && pwd )"

CONDA_PATH=$(ensureconda --conda --no-install | sed 's:/mamba$:/conda:')
MAMBA_PATH=$(ensureconda --mamba --no-install | sed 's:/conda$:/mamba:')

if [[ ! -f "$MAMBA_PATH" ]]; then
  echo "[EE] 'mamba' not found."
  exit 1
fi

if [[ ! -f "$CONDA_PATH" ]]; then
  echo "[EE] 'conda' not found."
  exit 1
fi

input_params="$1"

if [[ "${input_params}" == *"use_conda=yes"* ]] || [[ "$input_params" == *"use_pyenv=yes"* ]]; then
  echo "Virtual environment defined."
else
  input_params="use_conda=yes ${input_params}"
fi

# NOTE: FOR NOW IT IS JUST USED BY POETRY
USE_PYENV=0

if [[ "${input_params}" == *"use_makim=yes"* ]] || [[ "$input_params" == *"use_make=yes"* ]]; then
  echo "Automation task tool defined."
else
  input_params="use_makim=yes ${input_params}"
fi

if [[ "${input_params}" == *"use_pre_commit=yes"* ]]; then
  echo "pre-commit tool defined."
else
  input_params="use_pre_commit=yes ${input_params}"
fi

ENV_NAME=osl-python-package

OUTPUT_DIR="/tmp/osl"
rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

cookiecutter --no-input \
  --output-dir "${OUTPUT_DIR}" \
  "${PROJECT_PATH}/src/scicookie" \
  ${input_params}

cd "${OUTPUT_DIR}/${ENV_NAME}"


if [[ "${input_params}" == *"use_conda=yes"* ]]; then
  set +x
  eval "$($CONDA_PATH shell.bash hook)"
  mamba env create --file conda/dev.yaml --name "${ENV_NAME}" --yes
  conda activate "${ENV_NAME}"
  set -x
fi

if [[ "$input_params" == *"use_pyenv=yes"* ]]; then
  USE_PYENV=1
  set +x
  virtualenv "${ENV_NAME}"
  source "${ENV_NAME}/bin/activate"
  set -x
fi

# remove any path to scicookie environment
export PATH=$(echo $PATH| sed -E "s/[^:]+\/scicookie\/[^:]+//g")

BUILD_SYSTEM="others"

if command -v poetry &> /dev/null; then
  if [[ "$USE_PYENV" == "1" ]]; then
    poetry config virtualenvs.create true --local
  fi
  poetry install
elif command -v flit &> /dev/null; then
  flit install
elif command -v meson &> /dev/null; then
  BUILD_SYSTEM="mesonpy"
  pip install ".[dev]"
elif command -v pdm &> /dev/null; then
  pdm install
elif command -v hatch &> /dev/null; then
  pip install ".[dev]"
elif command -v maturin &> /dev/null; then
  BUILD_SYSTEM="maturin"
  pip install ".[dev]"
elif [ "$(pip list|grep -c scikit_build_core)" -ne "0" ]; then
  pip install ".[dev]"
elif [ "$(pip list|grep -c pybind11)" -ne "0" ]; then
  # Assuming you are inside the root of the CMake source directory
  pip install ".[dev]"
else
  # use setuptools
  pip install ".[dev]"
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

python -c "import osl_python_package as mypkg; assert mypkg.__version__ == '0.1.0'"

if [[ "$BUILD_SYSTEM" == "maturin" ]]; then
  python -c "from osl_python_package import add; add(1, 1)"
fi

if [[ "$BUILD_SYSTEM" == "mesonpy" ]]; then
  python -c "from osl_python_package import core; core.foo()"
fi

export PATH=${PATH_ORI}

echo '---------------------------- passed --------------------------'
cd "${PWD_ORI}"
