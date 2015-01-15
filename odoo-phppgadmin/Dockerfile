FROM fideloper/docker-nginx-php
MAINTAINER Esteban Echeverry <tebanep@gmail.com>
ENV REFRESHED_AT 2015-01-06

# Update and upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y

# Install PhpPgAdmin
RUN apt-get install -y phppgadmin

# Symlink php
RUN ln -s /usr/share/phppgadmin /var/www/phppgadmin

