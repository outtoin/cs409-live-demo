FROM phusion/baseimage:0.9.19

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

ENV TERM=xterm-256color

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install necessary packages
RUN apt-get update && \
        apt-get install -y software-properties-common vim libcurl4-openssl-dev libssl-dev fontconfig && \
        add-apt-repository ppa:jonathonf/python-3.6

#RUN add-apt-repository -y ppa:deadsnakes/ppa && \
#    apt-get update && \
#    apt-get install -y python3.6
RUN apt-get update -y && apt-get install -y python-dev build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
        apt-get install -y git


# Install Python requirements
RUN mkdir -p /usr/src/app
COPY requirements.txt /usr/src/app/
RUN python3.6 -m pip install --upgrade pip
RUN python3.6 -m pip install -r /usr/src/app/requirements.txt

# Copy the files from the host to the container
COPY . /usr/src/app
WORKDIR /usr/src/
RUN chmod 777 -R *

# Copy font
COPY ./NanumBarunGothicLight.ttf /usr/share/fonts/
RUN fc-cache -fv

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
