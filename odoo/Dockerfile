FROM ubuntu:14.04
MAINTAINER Esteban Echeverry <tebanep@gmail.com>


# --------------------------------------------------------------------------------
# Data container for Odoo and PostgreSQL.
# All volumes are mounted by containers
# that use "volumes-from" when run.
# --------------------------------------------------------------------------------
ENV REFRESHED_AT 2015-01-05

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
    htop \
    cron \
    supervisor

RUN mkdir -p /var/log/supervisor

# --------------------------------------------------------------------------------
# PostgreSQL
# Install the ERP's database
# --------------------------------------------------------------------------------
ENV POSTGRESQL_REFRESHED_AT 2015-01-05

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

USER postgres

RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER odoo WITH SUPERUSER PASSWORD 'odoo';" &&\
    createdb -O odoo odoo

RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

# Expose PostgreSQL's volumes
EXPOSE 5432

# Create PostgreSQL's volumes
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# --------------------------------------------------------------------------------
# Odoo
# Install the ERP
# --------------------------------------------------------------------------------
ENV ODOO_REFRESHED_AT 2015-01-05

USER root

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y

# Set utf-8 to python enconding
ENV PYTHONIOENCODING utf-8

# Install basic dev packages
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated -q libssl-dev \
    libyaml-dev \
    libjpeg-dev \
    libgeoip-dev \
    libffi-dev \
    libqrencode-dev \
    libfreetype6-dev \
    zlib1g-dev \
    libpq-dev

# Create libjpeg symlinks
RUN ln -s /usr/include/freetype2 /usr/local/include/freetype \
    && ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/ \
    && ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/ \
    && ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/

# Install pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip

# Install Odoo's dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-dateutil python-decorator python-docutils python-feedparser \
python-gdata python-gevent python-imaging python-jinja2 python-ldap python-libxslt1 python-lxml \
python-mako python-mock python-openid python-passlib python-psutil python-psycopg2 python-pybabel \
python-pychart python-pydot python-pyparsing python-pypdf python-reportlab python-requests \
python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-werkzeug \
python-xlwt python-yaml wkhtmltopdf

# Copy Odoo configuration file to configuration directory
RUN mkdir -p /etc/odoo
COPY openerp-server.conf /etc/odoo/openerp-server.conf
RUN chown -R odoo: /etc/odoo
RUN chmod -R 777 /etc/odoo

# Create Odoo addons directory
RUN mkdir -p /opt/odoo/addons
RUN chown -R odoo: /opt/odoo
RUN chmod -R 755 /opt/odoo

# Create Odoo log directory
RUN mkdir -p /var/log/odoo
RUN chown -R root:odoo /var/log/odoo
RUN chmod -R 755 /var/log/odoo

USER odoo

# Change to odoo home directory
WORKDIR /opt/odoo

# Download odoo from github
ENV ODOO_DOWNLOADED_AT 2015-01-06
RUN git clone https://www.github.com/odoo/odoo --depth 1 --branch 8.0 --single-branch

# Expose Odoo's ports
EXPOSE 8069
EXPOSE 8072

# Create Odoo's volumes
VOLUME ["/etc/odoo", "/opt/odoo/addons", "/var/log/odoo"]

# --------------------------------------------------------------------------------
# Entrypoint
# Set container's entrypoint
# --------------------------------------------------------------------------------
ENV ENTRYPOINT_REFRESHED_AT 2015-01-05

USER root

# Change to root directory
WORKDIR /

RUN pip install sh
ENV PGDATA = /var/lib/postgresql/9.3/main

COPY init.py /
RUN chmod +x init.py

COPY  backer /
RUN chmod -R +x /backer

# Create Backups' volumes
RUN mkdir -p /backups
RUN chmod 777 -R /backups
VOLUME ["/backups", "/etc/cron.d"]

COPY supervisord.conf.d/* /etc/supervisor/conf.d/

