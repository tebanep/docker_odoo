FROM ubuntu:14.04
MAINTAINER Esteban Echeverry <tebanep@gmail.com>
ENV REFRESHED_AT 2015-01-05

# Allow the automatic answer of dialogs
ENV DEBIAN_FRONTEND noninteractive

# Update and upgrade
RUN apt-get update
RUN apt-get dist-upgrade -y

# Set locales
RUN locale-gen fr_FR \
    && locale-gen en_US.UTF-8 \
    && dpkg-reconfigure locales \
    && update-locale LANG=en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 \
    && echo 'LANG="en_US.UTF-8"' > /etc/default/locale

# Install basic OS package
RUN apt-get install -y --allow-unauthenticated -q bzr \
    python \
    python-dev \
    python-setuptools \
    git \
    vim \
    wget \
    tmux \
    htop \
