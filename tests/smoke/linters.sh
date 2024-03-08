#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

 ${SMOKE_DIR}/base.sh "use_bandit=yes"
 ${SMOKE_DIR}/base.sh "use_coverage=yes"
 ${SMOKE_DIR}/base.sh "use_flake8=yes"
 ${SMOKE_DIR}/base.sh "use_isort=yes"
 ${SMOKE_DIR}/base.sh "use_mccabe=yes"
 ${SMOKE_DIR}/base.sh "use_mypy=yes"
 ${SMOKE_DIR}/base.sh "use_pre_commit=yes"
 ${SMOKE_DIR}/base.sh "use_prettier=yes"
 ${SMOKE_DIR}/base.sh "use_pydocstyle=yes"
 ${SMOKE_DIR}/base.sh "use_ruff=yes"
 ${SMOKE_DIR}/base.sh "use_shellcheck=yes"
 ${SMOKE_DIR}/base.sh "use_vulture=yes"
