#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=Default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=Material'
. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=Cinder'
. ${SMOKE_DIR}/base.sh 'documentation_engine=mkdocs mkdocs_theme=Readthedocs'
