# Cloudfoundry Test Cases

The following is a collection of test cases for cloudfoundry.

### Prerequisites

* Docker

### Installing

*  Review the [README.md](https://github.com/tosin2013/cloudfoundry-testcases/blob/master/buildimage/) under the buildimage folder.
* modify the pcf-env file for your enviornment

### Test Cases
#### create org and space
```
./create-org-space/create-org-space.sh pcf-env
```

#### delete org and space
```
./create-org-space/create-org-space.sh pcf-env
```
#### deploy sample app
* Deploy sample app [deployapp.sh]() currently uses the [spring-music](https://github.com/cloudfoundry-samples/spring-music) app from [cloud foundry](https://github.com/cloudfoundry-samples/spring-music).
```
./test-pas-deployment/deployapp.sh pcf-env
```

#### Test sample connectivity
```
python test-pas-deployment/test-deployed-app.py --filename output.csv --url https://yourapiendpoint.com
```

#### delete app
```
./delete-app/delete-app.sh pcf-env  appname
```

## Authors

* **Tosin Akinosho** - *Initial work* - [tosin2013](https://github.com/tosin2013)
