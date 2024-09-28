#!/usr/bin/env bash
echo "-------------------- Smoke test for ${1} -------------------"
set -ex

export PATH_ORI=${PATH}
export PWD_ORI=$(pwd)
export PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd ../.. && pwd )"

export CONDA_PATH=$(ensureconda --conda --no-install | sed 's:/mamba$:/conda:')
export MAMBA_PATH=$(ensureconda --mamba --no-install | sed 's:/conda$:/mamba:')

if [[ ! -f "$MAMBA_PATH" ]]; then
  echo "[EE] 'mamba' not found."
  exit 1
fi

if [[ ! -f "$CONDA_PATH" ]]; then
  echo "[EE] 'conda' not found."
  exit 1
fi

export input_params="$1"

if [[ "${input_params}" == *"use_conda=yes"* ]] || [[ "$input_params" == *"use_pyenv=yes"* ]]; then
  echo "Virtual environment defined."
else
  export input_params="use_conda=yes ${input_params}"
fi

# NOTE: FOR NOW IT IS JUST USED BY POETRY
export USE_PYENV=0

if [[ "${input_params}" == *"use_makim=yes"* ]] || [[ "$input_params" == *"use_make=yes"* ]]; then
  echo "Automation task tool defined."
else
  export input_params="use_makim=yes ${input_params}"
fi

if [[ "${input_params}" == *"use_pre_commit=yes"* ]]; then
  echo "pre-commit tool defined."
else
  export input_params="use_pre_commit=yes ${input_params}"
fi

export OUTPUT_DIR="/tmp/osl"
rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

cookiecutter --no-input \
  --output-dir "${OUTPUT_DIR}" \
  "${PROJECT_PATH}/src/scicookie" \
  ${input_params}

echo "${OUTPUT_DIR}"

set +ex

if [[ "${input_params}" == *"use_circleci=yes"* ]] && command -v circleci &> /dev/null; then
  pushd /tmp/osl/osl-python-package
  circleci config validate
  popd
fi
