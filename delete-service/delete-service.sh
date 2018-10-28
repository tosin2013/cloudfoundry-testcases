#/bin/bash
set -xe

if [[ "$#" -ne 3 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: delete-service.sh pcf-env appname servicename"
    exit $?
fi

source $1

if [[ ${USESKIPSSL} == "TRUE" ]]; then
    SKIPSSL="--skip-ssl-validation"
fi

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD} ${SKIPSSL} -o ${ORG} -s ${SPACE} || exit $?

cf target -o ${ORG} -s ${SPACE} || exit $?

cf unbind-service $2 $3 || exit $?

cf delete-service $3 -f || exit $?
