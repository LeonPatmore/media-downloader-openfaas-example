import os

import boto3

from logger import logger
from secrets import get_secret

access_key_id = get_secret("accessKeyId")
secretAccessKey = get_secret("secretAccessKey")
logger.info(f"AWS access key is [ {access_key_id} ]")

BUCKET_NAME = os.environ.get("BUCKET_NAME")
assert BUCKET_NAME
logger.info(f"Bucket name is [ {BUCKET_NAME} ]")

AWS_REGION = os.environ.get("AWS_REGION", "eu-west-1")
assert AWS_REGION
logger.info(f"AWS region [ {AWS_REGION} ]")

S3_CLIENT = boto3.client('s3',
                         region_name=AWS_REGION,
                         aws_access_key_id=access_key_id,
                         aws_secret_access_key=secretAccessKey)
