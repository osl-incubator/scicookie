#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh "code_of_conduct=contributor-covenant"
. ${SMOKE_DIR}/base.sh "code_of_conduct=citizen-code-of-conduct"
. ${SMOKE_DIR}/base.sh "code_of_conduct=numfocus-adapted-coc"
. ${SMOKE_DIR}/base.sh "code_of_conduct=python-adapted-coc"
. ${SMOKE_DIR}/base.sh "code_of_conduct=None"

. ${SMOKE_DIR}/base.sh "governance_document=numpy-governance"
. ${SMOKE_DIR}/base.sh "governance_document=sciml-governance"
. ${SMOKE_DIR}/base.sh "governance_document=None"

. ${SMOKE_DIR}/base.sh "roadmap_document=pytorch-ignite-roadmap"
. ${SMOKE_DIR}/base.sh "roadmap_document=None"
