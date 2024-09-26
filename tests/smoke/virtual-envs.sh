#!/usr/bin/env bash
set -ex

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh "use_conda=yes"
. ${SMOKE_DIR}/base.sh "use_pyenv=yes"

set +ex
