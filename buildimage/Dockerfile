FROM ubuntu:latest
RUN apt update && \
apt install -y default-jdk g++ make wget && \
apt update && \
apt install -y git wget curl  vim dnsutils  gnupg2 gnupg gnupg1 python python-pip
RUN wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -  && \
echo "deb https://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list
RUN apt update && \
apt install -y  cf-cli && \
pip install requests
RUN cd /root && \
git clone https://github.com/tosin2013/cloudfoundry-testcases.git

ENTRYPOINT ["/bin/bash"]
