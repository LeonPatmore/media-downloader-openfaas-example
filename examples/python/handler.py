import json

from flask import request
from werkzeug.datastructures import FileStorage

from .configuration import S3_CLIENT, BUCKET_NAME
from .logger import logger


def _upload_file(file: FileStorage):
    logger.info(f"Uploading file {file.filename}")
    S3_CLIENT.upload_fileobj(file, BUCKET_NAME, file.filename)


def handle(event, context):

    for file in request.files.values():
        _upload_file(file)

    data = request.form.to_dict()
    logger.info(json.dumps(data))
    logger.info(f"Hello! You said: " + str(event) + " | " + str(context))

    return {
        "statusCode": 200,
        "body": {
            "key": "value"
        },
        "headers": {
            "Content-Type": "application/json"
        }
    }
