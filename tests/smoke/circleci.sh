#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base-template.sh "use_circleci=yes use_conda=yes"
. ${SMOKE_DIR}/base-template.sh "use_circleci=yes use_pyenv=yes"
