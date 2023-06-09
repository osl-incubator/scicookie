#!/usr/bin/env bash

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh 'code_of_conduct="Contributor Covenant (projects of all sizes)"'
. ${SMOKE_DIR}/base.sh 'code_of_conduct="Citizen Code of Conduct (communities and events)"'
. ${SMOKE_DIR}/base.sh 'code_of_conduct="None"'
