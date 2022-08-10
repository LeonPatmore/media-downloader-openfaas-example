import logging
import os

import boto3

s3_client = boto3.client('s3')
logging.basicConfig(level=logging.DEBUG)


def handle(event, context):
    # s3_client.upload_file(file_name, bucket, object_name)

    logging.info(f"Hello! You said: " + event + " | " + context)

    return {
        "statusCode": 200,
        "body": {
            "key": "value"
        },
        "headers": {
            "Content-Type": "application/json"
        }
    }
