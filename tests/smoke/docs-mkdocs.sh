#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=material'
. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=cinder'
. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=readthedocs'
