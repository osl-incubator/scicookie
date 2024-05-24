#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs'
. ${SMOKE_DIR}/base.sh 'documentation_engine=jupyter-book'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(rst)'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(myst)'
. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto'
