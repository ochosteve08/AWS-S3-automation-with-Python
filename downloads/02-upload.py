import boto3
import os


#instantiate client

client = boto3.client('s3')

#set variables
bucket = 'esthree-2025'
cwr_path = os.path.dirname(os.path.abspath(__file__))  # Get current script's directory
file = 'report-lastyear.csv'
filename = os.path.join(cwr_path, '..', 'data', file)  # Move one level up and enter 'data'

# Check if file exists before opening
if not os.path.exists(filename):
    print(f"Error: File '{filename}' not found!")
else:
    with open(filename, 'rb') as data:
        client.upload_file(filename, bucket, file)
    print("File uploaded successfully!")


#load data into the bucket
client.upload_file(filename,bucket, file)