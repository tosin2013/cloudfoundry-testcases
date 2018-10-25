# PCF Dockerfile for testing

The following Dockerfile will be used to perform the tests.

## Getting Started

### Prerequisites

* Docker

### Installing

Build docker image on ubuntu
```
cd buildimage/ubuntu
docker build -t cloudfoundry-testcases:v1 .
```

Build docker image on alpinelinux
```
cd buildimage/alpinelinux
docker build -t cloudfoundry-testcases:v1 .
```

Get docker image

```
$ docker images
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
cloudfoundry-testcases   v1                  6ad72209032f        7 seconds ago       1.05GB
```

Start Docker Container
```
$ docker run -it cloudfoundry-testcases:v1
root@c17e808a7741:/#
```

Change to your directory to cloudfoundry-testcases
```
cd /root/cloudfoundry-testcases/
```

run scripts
