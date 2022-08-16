import logging
import boto3

from .secrets import get_secret

logging.basicConfig(level=logging.DEBUG)

access_key_id = get_secret("accessKeyId")
secretAccessKey = get_secret("secretAccessKey")
logging.info(f"AWS access key is {access_key_id}")

s3_client = boto3.client('s3',
                         region_name="eu-west-1",
                         aws_access_key_id=access_key_id,
                         aws_secret_access_key=secretAccessKey)


def handle(event, context):

    # s3_client.upload_file(file_name, bucket, object_name)

    with open('/var/openfaas/secrets/accessKeyId', 'rb') as data:
        s3_client.upload_fileobj(data, 'mybucket', 'example')

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
