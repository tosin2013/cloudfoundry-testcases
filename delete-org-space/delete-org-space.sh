#/bin/bash
set -xe

if [[ -z $1 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: delete-org-space.sh $1"
    exit $?
fi

source $1

if [[ ${USESKIPSSL} == "TRUE" ]]; then
    SKIPSSL="--skip-ssl-validation"
fi

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD} ${SKIPSSL} -o system -s system || exit $?

cf delete-space ${SPACE} -o $ORG || exit $?

cf delete-org ${ORG}  || exit $?

cf orgs || exit $?

cf spaces || exit $?
