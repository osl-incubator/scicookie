#!/usr/bin/env bash

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh "build_system=poetry"
. ${SMOKE_DIR}/base.sh "build_system=flit"
. ${SMOKE_DIR}/base.sh "build_system=mesonpy"
. ${SMOKE_DIR}/base.sh "build_system=setuptools"
. ${SMOKE_DIR}/base.sh "build_system=pdm"
. ${SMOKE_DIR}/base.sh "build_system=hatch"
. ${SMOKE_DIR}/base.sh "build_system=maturin"
. ${SMOKE_DIR}/base.sh "build_system=scikit-build-core"
