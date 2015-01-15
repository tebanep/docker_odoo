FROM tebanep/odoo-base
MAINTAINER Esteban Echeverry <tebanep@gmail.com>
ENV REFRESHED_AT 2015-01-05

# --------------------------------------------------------------------------------
# Data container for Odoo and PostgreSQL.
# All volumes are mounted by containers
# that use "volumes-from" when run.
# --------------------------------------------------------------------------------

# Copy Odoo configuration file to configuration directory
RUN mkdir -p /etc/odoo
COPY openerp-server.conf /etc/odoo/openerp-server.conf
RUN chown -R odoo: /etc/odoo
RUN chmod -R 755 /etc/odoo

# Create Odoo addons directory
RUN mkdir -p /opt/odoo/addons
RUN chown -R odoo: /opt/odoo/addons
RUN chmod -R 755 /opt/odoo/addons

# Create Odoo log directory
RUN mkdir -p /var/log/odoo
RUN chown root:odoo /var/log/odoo
RUN chmod -R 755 /var/log/odoo





# Create PostgreSQL configuration directory
RUN mkdir -p /etc/postgresql/9.3/main/
RUN chown -R postgres:postgres /etc/postgresql/9.3
RUN chmod 777 -R /etc/postgresql/9.3/main/
RUN chown postgres: /etc/postgresql

# Create PostgrSQL run directory and set permissions
RUN mkdir -p /var/run/postgresql
RUN chown postgres: /var/run/postgresql
RUN chmod 2775 /var/run/postgresql

# Create PostgreSQL log directory
RUN mkdir -p /var/log/postgresql
RUN chown -R root:postgres /var/log/postgresql
RUN chmod -R 1774 /var/log/postgresql

RUN mkdir -p /var/lib/postgresql/9.3/main
RUN chown -R postgres: /var/lib/postgresql/9.3
RUN chmod -R 700 /var/lib/postgresql/9.3



# Create Odoo volumes
USER odoo
VOLUME ["/etc/odoo", "/opt/odoo/addons", "/var/log/odoo"]

# Create PostgreSQL volumes
USER postgres
#VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

#VOLUME  ["/etc/postgresql"]
ENV HOLA=2

RUN ls -ln /var/lib/postgresql/9.3

VOLUME  ["/var/lib/postgresql"]
RUN ls -ln /var/lib/postgresql/9.3

# Bueno
#VOLUME  ["/var/log/postgresql"]

USER root
RUN echo "Data container for Odoo and its PostgreSQL database"



# Change to odoo home directory
USER odoo
WORKDIR /opt/odoo

# Download odoo from github
ENV ODOO_DOWNLOADED_AT 2015-01-06
RUN git clone https://www.github.com/odoo/odoo --depth 1 --branch 8.0 --single-branch

# Expose Odoo ports
EXPOSE 8069
EXPOSE 8072

# Create volumes
VOLUME ["/etc/odoo", "/opt/odoo/addons", "/var/log/odoo"]

RUN cat /etc/passwd

# Set command
CMD ["odoo/odoo.py", "-c", "/etc/odoo/openerp-server.conf"]
