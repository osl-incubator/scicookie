#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=jupyter-book jupyter_book_theme=Default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=jupyter-book jupyter_book_theme=PyData-sphinx-theme'
. ${SMOKE_DIR}/base.sh 'documentation_engine=jupyter-book jupyter_book_theme=Readthedocs-sphinx-theme'
