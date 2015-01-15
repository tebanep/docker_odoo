FROM ubuntu:14.04
MAINTAINER Esteban Echeverry <tebanep@gmail.com>
ENV REFRESHED_AT 2015-01-05

# --------------------------------------------------------------------------------
# Data container for Odoo and PostgreSQL.
# All volumes are mounted by containers
# that use "volumes-from" when run.
# --------------------------------------------------------------------------------

# add our users and groups first to make sure their IDs get assigned consistently,
# regardless of whatever dependencies get added

# Create postgres user
RUN adduser --system --shell /bin/bash --home=/var/lib/postgresql -c "PostgreSQL administrator" --group postgres

# Create odoo user
RUN adduser --system --shell /bin/bash --home=/opt/odoo -c "Odoo administrator" --group odoo

# Update and upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y

# Set locales
RUN DEBIAN_FRONTEND=noninteractive locale-gen fr_FR \
    && locale-gen en_US.UTF-8 \
    && dpkg-reconfigure locales \
    && update-locale LANG=en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 \
    && echo 'LANG="en_US.UTF-8"' > /etc/default/locale

# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y locales \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

# Install basic OS package
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated -q bzr \
    python \
    python-dev \
    python-setuptools \
    python-software-properties \
    software-properties-common \
    git \
    vim \
    wget \
    tmux \
    htop

