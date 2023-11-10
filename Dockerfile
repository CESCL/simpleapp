FROM jenkins/jenkins:lts-jdk11

USER root

# Install Python 3
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jenkins