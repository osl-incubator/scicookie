#!/usr/bin/env bash

#SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


. ${SMOKE_DIR}/base.sh "use_makim=yes use_make=no"
. ${SMOKE_DIR}/base.sh "use_makim=no use_make=yes"
