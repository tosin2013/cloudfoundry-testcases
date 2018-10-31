#/bin/bash
set -xe

if [[ -z $1  && -z ]]; then
    echo "Please pass enviornment file to be used during deployment."
    echo "USAGE: deployapp.sh pcf-env redis-plan"
    exit $?
fi

source $1

if [[ ${USESKIPSSL} == "TRUE" ]]; then
    SKIPSSL="--skip-ssl-validation"
fi

git clone https://github.com/pivotal-cf/cf-redis-example-app.git

cd cf-redis-example-app

cf login -a https://${PCFURL} -u ${USERNAME} -p ${PASSWORD} ${SKIPSSL} -o ${ORG} -s ${SPACE} || exit 1

cf target -o ${ORG} -s ${SPACE}

cf push redis-test-app --no-start
cf create-service p-redis $2 redis
cf bind-service redis-test-app redis
cf start redis-test-app

APPENDPOINT=$(cf app redis-test-app | grep routes | awk '{print $2}')
echo "APP ENDPONT: ${APPPROTOCALL}${APPENDPOINT}"
echo "Call the test-deployed-app.py script to test connectivity. "
echo "EXAMPLE: python test-pas-deployment/test-deployed-app.py --filename output.csv --url ${APPPROTOCALL}${APPENDPOINT}"
