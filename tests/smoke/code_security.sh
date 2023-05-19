#!/usr/bin/env bash

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh code_security "bandit"
. ${SMOKE_DIR}/base.sh code_security "None"
