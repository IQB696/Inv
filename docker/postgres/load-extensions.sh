#1/bin/bash

#psql -v ON_ERROR_STOP=1 -d "$POSTGRES_DB" --username "$POSTGRES_USER" << EOF
# CREATE EXTENSION postgis;
# CREATE EXTENSION postgis_topology;
# select current_database();
# create extension pg_trgm;
# select * FROM pg_extension;
#EOF
