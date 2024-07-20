#!/usr/bin/env bash
echo "-------------------- Smoke test for ${1} -------------------"

export PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd ../.. && pwd )"

source $PROJECT_PATH/tests/smoke/base-template.sh ${1}

set -ex

ENV_NAME=osl-python-package

cd "${OUTPUT_DIR}/${ENV_NAME}"

if [[ "${input_params}" == *"use_conda=yes"* ]]; then
  set +x
  eval "$($CONDA_PATH shell.bash hook)"
  mamba env create --file conda/dev.yaml --name "${ENV_NAME}" --yes
  conda activate "${ENV_NAME}"
  set -x
fi

if [[ "$input_params" == *"use_pyenv=yes"* ]]; then
  virtualenv "${ENV_NAME}"
  source "${ENV_NAME}/bin/activate"
  pip install -r requirements.txt
fi

# remove any path to scicookie environment
export PATH=$(echo $PATH| sed -E "s/[^:]+\/scicookie\/[^:]+//g")

BUILD_SYSTEM="others"

if command -v poetry &> /dev/null; then
  poetry install
elif command -v flit &> /dev/null; then
  flit install
elif command -v pixi &> /dev/null; then
  pixi install
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

set +ex
