import logging
import os

import boto3

s3_client = boto3.client('s3')
logging.basicConfig(level=logging.DEBUG)


def handle(req):
    # s3_client.upload_file(file_name, bucket, object_name)

    logging.info("Hello! You said: " + req)
    os.environ["content_type"] = "application/json"

    return {
        "id": "abc123"
    }
