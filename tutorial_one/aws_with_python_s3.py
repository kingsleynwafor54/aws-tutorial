# pip install boto3
import boto3
import os
import pandas as pd
# import logging
# Initialize a session using the Aws credentials

session=boto3.Session(
    aws_access_key_id='AKIAWZQJO4WO6JCBURFY',
    aws_secret_access_key='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',
    region_name='us-east-1'
)


# Create an S3 Client
s3=session.client('s3')

response = s3.list_buckets()
# List all s3 buckets
def get_listof_buckets():
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


#Create a bucket
# bucket_name='s3-bucket-kingsley1'
# s3.create_bucket(Bucket=bucket_name)
# get_listof_buckets()


# # Let's upload a file to our bucket
def upload_file_to_s3(filepath,bucket_name,key):
    # file_path=r'C:\Users\USER\Downloads\football.jpeg'
    # s3.upload_file(file_path,"s3-bucket-kingsley1","football.jpeg")
    # s3.upload_file('sample_data.csv',"s3-bucket-kingsley","sample_data.csv")
    s3.upload_file(filepath,bucket_name,key) 
# s3.upload_file('sample_data.csv',"s3-bucket-kingsley","sample_data.csv")



# s3.download_file('s3-bucket-kingsley1', 'football.jpeg', 'football.jpeg')
# s3.download_file('s3-bucket-kingsley', 'sample_data.csv', 'sample_data.csv')



#Deleting files in a bucket
# bucket_name = 's3-bucket-kingsley1'
# file_key = 'sample_data.csv'

# try:
#     # Delete the file
#     s3.delete_object(Bucket=bucket_name, Key=file_key)
#     print(f"File {file_key} deleted successfully from {bucket_name}")
    
# except Exception as e:
#     print(f"Error deleting file: {e}")




# CHECK ALL FILES IN A BUCKET
# try:
#     # List all objects in the bucket
#     objects = s3.list_objects_v2(Bucket=bucket_name)

#     # Check if objects were found
#     if 'Contents' in objects:
#         print(f"Files in {bucket_name}:")

#         # Iterate through the list of objects and print their keys (file paths)
#         for obj in objects['Contents']:
#             print(obj['Key'])
#     else:
#         print(f"No objects found in {bucket_name}")
# except Exception as e:
#     print(f"Error listing objects: {e}")

# Delete the bucket

# s3.delete_bucket(Bucket='s3-bucket-kingsley1')




