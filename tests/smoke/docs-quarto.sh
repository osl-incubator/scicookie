#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=cosmo'
. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=cerulean'
. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=materia'
