#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=Default'
. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=Cosmo'
. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=Cerulean'
. ${SMOKE_DIR}/base.sh 'documentation_engine=quarto quarto_theme=Materia'
