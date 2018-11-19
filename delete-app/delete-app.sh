#/bin/bash
set -xe

if [[ "$#" -ne 2 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: deleteapp.sh pcf-env appname"
    exit $?
fi

source $1

if [[ ${USESKIPSSL} == "TRUE" ]]; then
    SKIPSSL="--skip-ssl-validation"
fi

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD} ${SKIPSSL} -o ${ORG} -s ${SPACE} || exit $?

cf target -o ${ORG} -s ${SPACE} || exit $?

cf delete $2 -f -r || exit $?
