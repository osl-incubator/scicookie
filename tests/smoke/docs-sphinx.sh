#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(rst) sphinx_theme=default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(rst) sphinx_theme=readthedocs'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(rst) sphinx_theme=pydata'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(myst) sphinx_theme=default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(myst) sphinx_theme=readthedocs'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(myst) sphinx_theme=pydata'
