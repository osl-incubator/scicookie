#!/usr/bin/env bash

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ROADMAP=""
. ${SMOKE_DIR}/base.sh "roadmap_document=pytorch-ignite-roadmap"
. ${SMOKE_DIR}/base.sh "roadmap_document=None"
