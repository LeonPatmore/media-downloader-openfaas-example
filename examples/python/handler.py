import os

import boto3

s3_client = boto3.client('s3')


def handle(req):
    # s3_client.upload_file(file_name, bucket, object_name)

    print("Hello! You said: " + req)

    return {
        "id": "abc123"
    }


def _response():
    os.environ["content_type"] = "application/json"
