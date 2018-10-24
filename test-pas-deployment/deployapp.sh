#/bin/bash
set -xe

if [[ -z $1 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: deployapp.sh $1"
    exit $?
fi

git clone https://github.com/cloudfoundry-samples/spring-music

cd spring-music

./gradlew clean assemble

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD}
