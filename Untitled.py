import pandas as pd
from dotenv import load_dotenv
import boto3

import logging
from botocore.exceptions import ClientError


# Resource
s3 = boto3.resource('s3')

# bucket
bucket = s3.Bucket("my-first-s3-bucket-u")

## uploading a file
bucket.upload_file(Key='synthetic_data3.csv', Filename='data/synthetic_data3.csv')
bucket.download_file(Key='synthetic_data1.csv', Filename='downloaded_data.csv')

for bucket in s3.buckets.all():
    print(bucket.name)


## create buckets
def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#create_bucket('my-second-s3-bucket-u', region="ap-southeast-2")

for bucket in s3.buckets.all():
    print(bucket.name)


boto3.Session().region_name
session


aws s3 presign s3://my-first-s3-bucket-u/synthetic_data1.csv --expires-in 2 --region ap-southeast-2 --endpoint-url https://s3.ap-southeast-2.amazonaws.com

aws s3 presign s3://amzn-s3-demo-bucket/mydoc.txt --expires-in 604800 