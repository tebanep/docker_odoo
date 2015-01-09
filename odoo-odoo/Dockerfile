# Odoo installation based in theopensourcerer.com and vauxoo guide
FROM tebanep/odoo-ubuntu
MAINTAINER Esteban Echeverry <tebanep@gmail.com>
ENV REFRESHED_AT 2015-01-06

RUN apt-get update
RUN apt-get dist-upgrade -y

# Set utf-8 to python enconding
ENV PYTHONIOENCODING utf-8

# Install basic dev packages
RUN apt-get install -y --allow-unauthenticated -q libssl-dev \
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
RUN apt-get install -y python-pip

# Install python dependencies
RUN apt-get install -y python-dateutil python-decorator python-docutils python-feedparser \
python-gdata python-gevent python-imaging python-jinja2 python-ldap python-libxslt1 python-lxml \
python-mako python-mock python-openid python-passlib python-psutil python-psycopg2 python-pybabel \
python-pychart python-pydot python-pyparsing python-pypdf python-reportlab python-requests \
python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-werkzeug \
python-xlwt python-yaml wkhtmltopdf

# Create odoo user
RUN adduser --system --home=/opt/odoo --group odoo

RUN mkdir -p /var/log/odoo
RUN chown odoo:root /var/log/odoo

# Change to odoo home directory
USER odoo
WORKDIR /opt/odoo

# Download odoo from github
ENV ODOO_DOWNLOADED_AT 2015-01-06
RUN git clone https://www.github.com/odoo/odoo --depth 1 --branch 8.0 --single-branch

# Copy odoo configuration file
USER root
RUN mkdir -p /etc/odoo
COPY openerp-server.conf /etc/odoo/openerp-server.conf
RUN chown -R odoo: /etc/odoo
RUN chmod -R 755 /etc/odoo

# Create addons directory
USER odoo
RUN mkdir -p /opt/odoo/addons

# Expose Odoo ports
EXPOSE 8069
EXPOSE 8072

# Create volumes
VOLUME ["/etc/odoo", "/opt/odoo/addons", "/var/log/odoo"]

# Set command
CMD ["odoo/odoo.py", "-c", "/etc/odoo/openerp-server.conf"]
