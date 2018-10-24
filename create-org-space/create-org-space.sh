#/bin/bash
set -xe

if [[ -z $1 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: create-org-space.sh $1"
    exit $?
fi

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD}

cf create-org $ORG  || exit $?

cf create-space ${SPACE} -o $ORG || exit $?

cf spaces || exit $?
