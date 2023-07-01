# Environment Variables

This file defines different environment variables used in all X-Pkg software.

## Registry

### Required Variables

- `AUTH_SECRET` -- The secret used to sign authorization tokens.
- `AWS_ACCESS_KEY_ID` -- The access key for AWS.
- `AWS_SECRET_ACCESS_KEY` -- The AWS secret access key.
- `EMAIL_FROM` -- The email address that is sending the email.
- `EMAIL_PASSWORD` -- The password of the account to login to the email sending service.
- `EMAIL_USER` -- The username of the account to login to the email sending service.
- `EMAIL_VERIFY_SECRET` -- The secret used to sign email verification tokens.
- `JOBS_SERVICE_ADDR` -- The address of the X-Pkg jobs service. Include the port number with a colon if not on port 443 (assumes HTTPS).
- `JOBS_SERVICE_PASSWORD` -- The password sent to the X-Pkg jobs service during the handshake.
- `MONGODB_IP` -- The address (or URI) of the MongoDB Atlas server.
- `MONGODB_KEY_PATH` -- The absolute path to the certificate for MongoDB atlas.
- `PASSWORD_RESET_SECRET` -- The secret used to sign password reset tokens.
- `RECAPTCHA_SECRET` -- The secret shared between reCAPTCHA and the server. 
- `SERVER_TRUST_HASH` -- The hash of the trust key recieved from the X-Pkg jobs service during the handshake.

### Optional Variables

- `PORT` -- Only used to changed the port that the registry listens on. Defaults to 443.
- `RECAPTCHA_DISABLE` -- Set to 1 in order to disable server-side reCAPTCHA validation.

## Jobs Service

### Required Variables

- `HTTPS_KEY_PATH` -- The path to the private key file for HTTPS.
- `HTTPS_CERT_PATH` -- The path to the cert file for HTTPS.
- `HTTPS_CHAIN_PATH` -- The path to the chain file used for HTTPS.
- `JOBS_SERVICE_HASH` -- The hash of the password that the worker sends during the handshake.
- `MONGODB_IP` -- The address (or URI) of the MongoDB Atlas server.
- `MONGODB_KEY_PATH` -- The absolute path to the certificate for MongoDB atlas.
- `SERVER_TRUST_KEY` -- The trust key that is sent to a worker during the handshake.

### Optional Variables

- `PORT` -- Only used to changed the port that the registry listens on. Defaults to 443.