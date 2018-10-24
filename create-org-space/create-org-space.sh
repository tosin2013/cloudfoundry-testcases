#/bin/bash
set -xe

if [[ -z $1 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: create-org-space.sh $1"
    exit $?
fi

source $1

if [[ ${USESKIPSSL} == "TRUE" ]]; then
    SKIPSSL="--skip-ssl-validation"
fi

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD} ${SKIPSSL} -o system -s system || exit $?

cf create-org ${ORG}  || exit $?

cf create-space ${SPACE} -o $ORG || exit $?

cf orgs || exit $?

cf target -o ${ORG} -s ${SPACE} || exit $?

cf spaces || exit $?
