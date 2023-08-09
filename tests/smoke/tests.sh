SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh "use_pytest=yes"
. ${SMOKE_DIR}/base.sh "use_pytest=yes use_hypothesis=yes"
# NOTE: it is necessary to improve the workflow when
#       use_pytest=no and use_hypothesis=yes
# . ${SMOKE_DIR}/base.sh "use_hypothesis=yes"
