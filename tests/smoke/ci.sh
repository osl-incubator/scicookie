#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# run the complete smoke tests
. ${SMOKE_DIR}/base.sh "use_circleci=yes use_conda=yes"
. ${SMOKE_DIR}/base.sh "use_circleci=yes use_pyenv=yes"

# check the CI files from template
. ${SMOKE_DIR}/base-template.sh "use_circleci=yes use_conda=yes"
pushd /tmp/osl/osl-python-package
  circleci config validate
popd

. ${SMOKE_DIR}/base-template.sh "use_circleci=yes use_pyenv=yes"
pushd /tmp/osl/osl-python-package
  circleci config validate
popd
