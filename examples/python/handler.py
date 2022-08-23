from flask import request
from werkzeug.datastructures import FileStorage

try:
    from configuration import S3_CLIENT, BUCKET_NAME
except ModuleNotFoundError:
    from .configuration import S3_CLIENT, BUCKET_NAME
try:
    from logger import logger
except ModuleNotFoundError:
    from .logger import logger


def _upload_file(file: FileStorage) -> str:
    logger.info(f"Uploading file {file.filename}")
    S3_CLIENT.upload_fileobj(file, BUCKET_NAME, file.filename)
    return file.filename


def handle(event, context):
    filenames = list()
    for file in request.files.values():
        filenames.append(_upload_file(file))

    logger.info(f"Successfully uploaded {filenames}")

    return {
        "statusCode": 200,
        "body": {
            "files": filenames
        },
        "headers": {
            "Content-Type": "application/json"
        }
    }
