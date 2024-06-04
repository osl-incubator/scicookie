#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(rst) sphinx_theme=Default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(rst) sphinx_theme=Readthedocs'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(rst) sphinx_theme=PyData'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(myst) sphinx_theme=Default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(myst) sphinx_theme=Readthedocs'
. ${SMOKE_DIR}/base.sh 'documentation_engine=sphinx(myst) sphinx_theme=PyData'
