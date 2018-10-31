#/bin/bash
set -xe

if [[ -z $1 ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: deployapp.sh $1"
    exit $?
fi

source $1
PLAN="standard"
if [[ ${USESKIPSSL} == "TRUE" ]]; then
    SKIPSSL="--skip-ssl-validation"
fi

git clone https://github.com/cloudfoundry-community/cf-rabbitmq-example-app.git

cd cf-rabbitmq-example-app


cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD} ${SKIPSSL} -o ${ORG} -s ${SPACE} || exit 1

cf target -o ${ORG} -s ${SPACE}

cf push rabbitmq-test-app --no-start
cf create-service p-rabbitmq $PLAN rabbitmq
cf bind-service rabbitmq-test-app rabbitmq
cf start rabbitmq-test-app

APPENDPOINT=$(cf app rabbitmq-test-app | grep routes | awk '{print $2}')
echo "APP ENDPONT: ${APPPROTOCALL}${APPENDPOINT}"
echo "Call the test-rabbitmq-app.py script to test connectivity. "
echo "EXAMPLE: python test-rabbitmq-deployment/test-rabbitmq-app.py --filename output.csv --url ${APPPROTOCALL}${APPENDPOINT}"
