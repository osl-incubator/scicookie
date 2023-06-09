#!/usr/bin/env bash

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh "governance=\\\"NumPy governance document\\\""
. ${SMOKE_DIR}/base.sh "governance=\\\"SciML governance document\\\""
. ${SMOKE_DIR}/base.sh "governance=\\\"None\\\""
