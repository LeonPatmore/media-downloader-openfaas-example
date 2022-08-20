import json

from flask import request

from .logger import logger


def handle(event, context):
    # with open('/var/openfaas/secrets/accessKeyId', 'rb') as data:
    #     s3_client.upload_fileobj(data, BUCKET_NAME, 'example')

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
