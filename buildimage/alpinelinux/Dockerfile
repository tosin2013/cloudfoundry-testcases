FROM alpine:latest
RUN apk add --no-cache vim openjdk7-jre git python py-pip curl
RUN pip install requests
RUN cd /tmp && \
    curl -L "https://packages.cloudfoundry.org/stable?release=linux64-binary&source=github" | tar -zx && \
    mv cf /usr/local/bin
RUN cd /root && \
git clone https://github.com/tosin2013/cloudfoundry-testcases.git
ENTRYPOINT ["/bin/sh"]

