FROM ubuntu:14.04
MAINTAINER Esteban Echeverry <tebanep@gmail.com>
ENV REFRESHED_AT 2015-01-05

#  Allow the automatic answer of dialogs
ENV DEBIAN_FRONTEND noninteractive

#  Set utf-8 to python enconding
ENV PYTHONIOENCODING utf-8

#  Update and upgrade
RUN apt-get update
RUN apt-get dist-upgrade -y

#  Install basic OS package
RUN apt-get install -y --allow-unauthenticated -q bzr \
    python \
    python-dev \
    python-setuptools \
    git \
    vim \
    wget \
    tmux \
    htop

#  Add git config data to root user. (Required to use git command)
#RUN git config --global user.name oca_docker \
#    && git config --global user.email hello@oca.com

#  Install basic dev packages
RUN apt-get install -y --allow-unauthenticated -q libssl-dev \
    libyaml-dev \
    libjpeg-dev \
    libgeoip-dev \
    libffi-dev \
    libqrencode-dev \
    libfreetype6-dev \
    zlib1g-dev \
    libpq-dev

#  Create libjpeg symlinks
RUN ln -s /usr/include/freetype2 /usr/local/include/freetype \
    && ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/ \
    && ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/ \
    && ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/

#  Installing pip
RUN apt-get install -y python-pip
