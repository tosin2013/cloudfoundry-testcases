FROM alpine:latest
RUN apk add --no-cache vim git python py-pip curl
RUN pip install requests
RUN cd /tmp && \
    curl -L "https://packages.cloudfoundry.org/stable?release=linux64-binary&source=github" | tar -zx && \
    mv cf /usr/local/bin
RUN cd /root && \
git clone https://github.com/tosin2013/cloudfoundry-testcases.git
# https://github.com/sgerrand/alpine-pkg-glibc/releases
RUN apk --update add curl ca-certificates tar && \
    curl -Ls https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk > /tmp/glibc-2.28-r0.apk  && \
    apk add --allow-untrusted /tmp/glibc-2.28-r0.apk
    # Download and unarchive Java
RUN mkdir -p /opt && \
   cd /opt  &&\
   curl -C - -LR#OH "Cookie: oraclelicense=accept-securebackup-cookie" -k 'http://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz' &&\
   tar -zxvf jdk-8u191-linux-x64.tar.gz &&\
    ln -s /opt/jdk1.8.0_191 /opt/jdk &&\
    rm -rf /opt/jdk/*src.zip \
           /opt/jdk/lib/missioncontrol \
           /opt/jdk/lib/visualvm \
           /opt/jdk/lib/*javafx* \
           /opt/jdk/jre/lib/plugin.jar \
           /opt/jdk/jre/lib/ext/jfxrt.jar \
           /opt/jdk/jre/bin/javaws \
           /opt/jdk/jre/lib/javaws.jar \
           /opt/jdk/jre/lib/desktop \
           /opt/jdk/jre/plugin \
           /opt/jdk/jre/lib/deploy* \
           /opt/jdk/jre/lib/*javafx* \
           /opt/jdk/jre/lib/*jfx* \
           /opt/jdk/jre/lib/amd64/libdecora_sse.so \
           /opt/jdk/jre/lib/amd64/libprism_*.so \
           /opt/jdk/jre/lib/amd64/libfxplugins.so \
           /opt/jdk/jre/lib/amd64/libglass.so \
           /opt/jdk/jre/lib/amd64/libgstreamer-lite.so \
           /opt/jdk/jre/lib/amd64/libjavafx*.so \
           /opt/jdk/jre/lib/amd64/libjfx*.so

# Set environment
ENV JAVA_HOME /opt/jdk
ENV PATH ${PATH}:${JAVA_HOME}/bin


ENTRYPOINT ["/bin/sh"]
