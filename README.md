# Media Downloader Openfaas Example

## Requirements

- python3.7 (for local testing), install using pyenv
- pipenv
- kubectl
- minikube
- base64

## Running Tests

`make test`

## Local

### Build

`make buid-local tag=abc123`

### Deploy

`make deploy-local tag=abc123`

## OpenFaas

https://github.com/openfaas/faas-netes/blob/master/chart/openfaas/README.md

### UI

Port forward the `gateway-external` service.

### Logging

Since the stdout of functions is piped into the http response, we can not use std out for logging.

Setting `combine_output: false` allows you to log to stderr.

### Secrets

Secrets use K8s secrets.

This is automated via the `Makefile`. Please ensure you have a `.env. file in the root of the project with the following:

```
export AWS_ACCESS_KEY_ID="my-id"
export AWS_SECRET_ACCESS_KEY="my-secret-key"
export BUCKET_NAME="media-upload-leonpatmore"
```

### Limitations

- No easy way to exclude folders from the build (i.e. the test folder).
- Logging to stderr is not clean.
- Tagging strategy is not ideal, since every time you want to build a new image, you must generate a new git commit.
- Can't inject secrets as env vars, you have to read them from a file system.
