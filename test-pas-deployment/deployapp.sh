#/bin/bash
set -xe

if [[ -z $1 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: deployapp.sh $1"
    exit $?
fi

source $1

if [[ ${USESKIPSSL} == "TRUE" ]]; then
    SKIPSSL="--skip-ssl-validation"
fi

git clone https://github.com/cloudfoundry-samples/spring-music

cd spring-music

./gradlew clean assemble

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD} ${SKIPSSL} -o ${ORG} -s ${SPACE} || exit 1

cf target -o ${ORG} -s ${SPACE}

cf push

APPENDPOINT=$(cf app spring-music | grep routes | awk '{print $2}')
echo "APP ENDPONT: ${APPPROTOCALL}${APPENDPOINT}"
echo "Call the test-deployed-app.py script to test connectivity. "
echo "EXAMPLE: python test-deployed-app.py --filename output.csv --url ${APPPROTOCALL}${APPENDPOINT}"
