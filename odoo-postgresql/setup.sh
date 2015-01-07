#!/bin/bash
echo "******CREATING DOCKER DATABASE******"
gosu postgres postgres --single <<- EOSQL
   CREATE DATABASE odoo;
   CREATE USER odoo;
   ALTER USER odoo WITH PASSWORD 'odoo';
   GRANT ALL PRIVILEGES ON DATABASE odoo to odoo;
EOSQL
echo ""
echo "******DOCKER DATABASE CREATED******"
