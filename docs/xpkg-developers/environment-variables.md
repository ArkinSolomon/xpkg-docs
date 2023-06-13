# Environment Variables

This file defines different environment variables used in X-Pkg servers and/or services.

## Registry

### Required Variables

- `AWS_ACCESS_KEY_ID` -- The access key for AWS.
- `AWS_SECRET_ACCESS_KEY` -- The AWS secret access key.
- `AUTH_SECRET` -- The secret used to sign authorization tokens.
- `PASSWORD_RESET_SECRET` -- The secret used to sign password reset tokens.
- `EMAIL_VERIFY_SECRET` -- The secret used to sign email verification tokens.
- `EMAIL_USER` -- The username of the account to login to the email sending service.
- `EMAIL_PASSWORD` -- The password of the account to login to the email sending service.
- `EMAIL_FROM` -- The email address that is sending the email.
- `JOBS_SERVICE_ADDR` -- The address of the X-Pkg jobs service.
- `JOBS_SERVICE_PORT` -- The port of the X-Pkg jobs service.
- `JOBS_SERVICE_PASSWORD` -- The password sent to the X-Pkg jobs service during the handshake.
- `SERVER_TRUST_HASH` -- The hash of the trust key recieved from the X-Pkg jobs service during the handshake.

### Optional Variables

- `PORT` -- Only used to changed the port that the registry listens on. Defaults to 5020.

### Implementation Specific Variables

- `MYSQL_DB_USER` -- The username of the login for the MySql database (only required if using a MySql database implementation).
- `MYSQL_DB_PASSWORD` -- The password to login to the MySql database (only required if using a MySql database implementation).
- `MYSQL_DB_ADDR` -- The address of the MySql database (only required if using a MySql database implementation).
- `MYSQL_DB_NAME` -- The name of the database that contains all of the X-Pkg tables (only required if using a MySql database implementation).

## Jobs Service

All environment variables defined here are required for the jobs service to run properly.

- `DB_USER` -- The username used to login to the jobs database.
- `DB_PASSWORD` -- The password used to login to the jobs database.
- `DB_ADDR` -- The address of the jobs database.
- `DB_NAME` -- The name of the jobs database.
- `SERVER_TRUST_KEY` -- The trust key that is sent to a worker during the handshake.
- `JOBS_SERVICE_HASH` -- The hash of the password that the worker sends during the handshake.
