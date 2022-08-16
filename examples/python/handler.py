import logging
import os

import boto3

from .secrets import get_secret

logging.basicConfig(level=logging.DEBUG)

access_key_id = get_secret("accessKeyId")
secretAccessKey = get_secret("secretAccessKey")
logging.info(f"AWS access key is [ {access_key_id} ]")

BUCKET_NAME = os.environ.get("BUCKET_NAME")
assert BUCKET_NAME

logging.info(f"Bucket name is [ {BUCKET_NAME} ]")

s3_client = boto3.client('s3',
                         region_name="eu-west-1",
                         aws_access_key_id=access_key_id,
                         aws_secret_access_key=secretAccessKey)


def handle(event, context):
    with open('/var/openfaas/secrets/accessKeyId', 'rb') as data:
        s3_client.upload_fileobj(data, BUCKET_NAME, 'example')

    logging.info(f"Hello! You said: " + str(event) + " | " + str(context))

    return {
        "statusCode": 200,
        "body": {
            "key": "value"
        },
        "headers": {
            "Content-Type": "application/json"
        }
    }
