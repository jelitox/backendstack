#!/bin/bash

# Immediately exits if any error occurs during the script
# execution. If not set, an error could occur and the
# script would continue its execution.
set -o errexit


# Creating an array that defines the environment variables
# that must be set. This can be consumed later via arrray
# variable expansion ${REQUIRED_ENV_VARS[@]}.
readonly REQUIRED_ENV_VARS=(
  "PG_DB_USER"
  "PG_DB_PASSWORD"
  "PG_DB_DATABASE_TEST"
  "PG_DB_DATABASE_PROD"
  "POSTGRES_USER")


# Main execution:
# - verifies if all environment variables are set
# - runs the SQL code to create user and database
main() {
  check_env_vars_set
  init_db_dev
  init_db_prod
  init_db_test
  init_create_extension_dev
  init_create_extension_prod
  init_create_extension_test
  init_users
}


# Checks if all of the required environment
# variables are set. If one of them isn't,
# echoes a text explaining which one isn't
# and the name of the ones that need to be
check_env_vars_set() {
  for required_env_var in ${REQUIRED_ENV_VARS[@]}; do
    if [[ -z "${!required_env_var}" ]]; then
      echo "Error:
    Environment variable '$required_env_var' not set.
    Make sure you have the following environment variables set:
      ${REQUIRED_ENV_VARS[@]}
Aborting."
      exit 1
    fi
  done
}


# Performs the initialization in the already-started PostgreSQL
# using the preconfigured POSTGRE_USER user.


init_db_dev() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
     CREATE DATABASE bs_dev;
EOSQL
}
init_create_extension_dev() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname bs_dev  <<-EOSQL
  CREATE EXTENSION btree_gin;
  CREATE EXTENSION btree_gist;
  CREATE EXTENSION hstore;
  CREATE EXTENSION tablefunc;
  CREATE EXTENSION "uuid-ossp";
   CREATE SCHEMA base;
EOSQL
}
init_db_prod() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
     CREATE DATABASE $PG_DB_DATABASE_PROD;
EOSQL
}
init_db_test() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
     CREATE DATABASE $PG_DB_DATABASE_TEST;
EOSQL
}

init_users() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
     CREATE USER $PG_DB_USER WITH PASSWORD '$PG_DB_PASSWORD';
     CREATE USER "bsroot" WITH PASSWORD '$PG_DB_PASSWORD';
     ALTER USER $PG_DB_USER WITH SUPERUSER;
     ALTER USER  "bsroot" WITH SUPERUSER;
     GRANT ALL PRIVILEGES ON DATABASE $PG_DB_DATABASE_PROD TO $PG_DB_USER;
     GRANT ALL PRIVILEGES ON DATABASE $PG_DB_DATABASE_TEST TO $PG_DB_USER;
     GRANT ALL PRIVILEGES ON DATABASE bs_dev TO $PG_DB_USER;
     GRANT ALL PRIVILEGES ON DATABASE bs_dev TO "bsroot";
     GRANT ALL PRIVILEGES ON DATABASE $PG_DB_DATABASE_PROD TO "bsroot";
     GRANT ALL PRIVILEGES ON DATABASE $PG_DB_DATABASE_TEST TO "bsroot";
EOSQL
}

init_create_extension_prod() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$PG_DB_DATABASE_PROD"  <<-EOSQL
  CREATE EXTENSION btree_gin;
  CREATE EXTENSION btree_gist;
  CREATE EXTENSION hstore;
  CREATE EXTENSION tablefunc;
  CREATE EXTENSION "uuid-ossp";
EOSQL
}

init_create_extension_test() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$PG_DB_DATABASE_TEST"  <<-EOSQL
  CREATE EXTENSION btree_gin;
  CREATE EXTENSION btree_gist;
  CREATE EXTENSION hstore;
  CREATE EXTENSION tablefunc;
  CREATE EXTENSION "uuid-ossp";
EOSQL
}


# Executes the main routine with environment variables
# passed through the command line. We don't use them in
# this script but now you know 🤓
main "$@"
