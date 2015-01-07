# Odoo installation based in theopensourcerer.com guide
FROM tebanep/odoo-ubuntu
MAINTAINER Esteban Echeverry <tebanep@gmail.com>
ENV REFRESHED_AT 2015-01-06

RUN apt-get update
RUN apt-get dist-upgrade -y

RUN useradd -d /opt/odoo -m odoo

# Install python dependencies
RUN apt-get install -y python-dateutil python-decorator python-docutils python-feedparser \
python-gdata python-gevent python-imaging python-jinja2 python-ldap python-libxslt1 python-lxml \
python-mako python-mock python-openid python-passlib python-psutil python-psycopg2 python-pybabel \
python-pychart python-pydot python-pyparsing python-pypdf python-reportlab python-requests \
python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-werkzeug \
python-xlwt python-yaml wkhtmltopdf

# Change to odoo home directory
USER odoo
WORKDIR /opt/odoo

# Download odoo from github
ENV ODOO_DOWNLOADED_AT 2015-01-06
RUN git clone https://www.github.com/odoo/odoo --depth 1 --branch 8.0 --single-branch

# Set encoding
USER root
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

# Copy odoo configuration file
RUN mkdir -p /etc/odoo
COPY openerp-server.conf /etc/odoo/openerp-server.conf
RUN chown -R odoo: /etc/odoo
RUN chmod -R 755 /etc/odoo

#VOLUME ["/etc/odoo", "/opt/odoo/addons", "/var/log/odoo"]

# Set entrypoint
USER odoo
ENTRYPOINT ["/opt/odoo/odoo/odoo.py"]
CMD ["-c", "/opt/odoo/openerp-server.conf"]
