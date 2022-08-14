# Media Downloader Openfaas Example

## OpenFaas

https://github.com/openfaas/faas-netes/blob/master/chart/openfaas/README.md

### UI

Port forward the `gateway-external` service.

### Logging

Since the stdout of functions is piped into the http response, we can not use std out for logging.

Setting `combine_output: false` allows you to log to stderr.

### Limitations

- No easy way to exclude folders from the build (i.e. the test folder).
- Logging to stderr is not clean.
- Tagging strategy is not ideal, since every time you want to build a new image, you must generate a new git commit.
- Can't inject secrets as env vars, you have to read them from a file system.
