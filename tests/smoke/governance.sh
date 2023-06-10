#!/usr/bin/env bash

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh "governance_document=numpy-governance"
. ${SMOKE_DIR}/base.sh "governance_document=sciml-governance"
. ${SMOKE_DIR}/base.sh "governance_document=None"
