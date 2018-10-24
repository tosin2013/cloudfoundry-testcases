FROM ubuntu:latest
RUN apt update && \
apt install -y ruby ruby-dev g++ make wget && \
apt update && \
apt install -y git wget curl  vim dnsutils  gnupg2 gnupg gnupg1 python
RUN wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -  && \
echo "deb https://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list
RUN apt update && \
apt install -y  cf-cli
ENTRYPOINT ["/bin/bash"]
