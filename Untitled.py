import pandas as pd
from dotenv import load_dotenv
import boto3

# Resource
s3 = boto3.resource('s3')

# bucket
bucket = s3.Bucket("my-first-s3-bucket-u")

## uploading a file
bucket.upload_file(Key='synthetic_data3.csv', Filename='data/synthetic_data3.csv')

bucket.download_file(Key='synthetic_data1.csv', Filename='downloaded_data.csv')
