# pip install boto3
import boto3
import os
import pandas as pd
# import logging
# Initialize a session using the Aws credentials

session=boto3.Session(
    aws_access_key_id='AKIAWZQJO4WOXT3S7FOQ',
    aws_secret_access_key='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',
    region_name='us-east-1'
)


# Create an S3 Client
s3=session.client('s3')


# List all s3 
response = s3.list_buckets()
def get_listof_buckets():
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


#Create a bucket

def create_s3_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    get_listof_buckets()


# # Let's upload a file to our bucket
def upload_file_to_s3(filepath,bucket_name,key):
    s3.upload_file(filepath,bucket_name,key) 


# downloading file from aws s3 bucket
def downloading_files_s3(bucket_name, object_name, file_name):
    s3.download_file(bucket_name, object_name, file_name)



#Deleting files in a bucket
def delete_file_s3(bucket_name,file_key):
    try:
        # Delete the file
        s3.delete_object(Bucket=bucket_name, Key=file_key)
        print(f"File {file_key} deleted successfully from {bucket_name}")
        
    except Exception as e:
        print(f"Error deleting file: {e}")




# CHECK ALL FILES IN A BUCKET
def checking_all_files_from_aws_s3_bucket(bucket_name):
    try:
        # List all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)

        # Check if objects were found
        if 'Contents' in objects:
            print(f"Files in {bucket_name}:")

            # Iterate through the list of objects and print their keys (file paths)
            for obj in objects['Contents']:
                print(obj['Key'])
        else:
            print(f"No objects found in {bucket_name}")
    except Exception as e:
        print(f"Error listing objects: {e}")

# Delete the bucket
def delete_s3_bucket(bucket_name):
    s3.delete_bucket(Bucket=bucket_name)


bucket_name='s3-bucket-kingsley1'
bucket_name = 's3-bucket-kingsley1'
file_key = 'sample_data.csv'
get_listof_buckets()
create_s3_bucket(bucket_name)
upload_file_to_s3('sample_data.csv',bucket_name,"sample_data.csv")
downloading_files_s3(bucket_name, 'sample_data.csv', "sample_data1.csv")
delete_file_s3(bucket_name,file_key)
checking_all_files_from_aws_s3_bucket(bucket_name)
delete_s3_bucket(bucket_name)

