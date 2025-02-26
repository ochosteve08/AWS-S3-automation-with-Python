import boto3
import os
from datetime import datetime


# Instantiate S3 client
client = boto3.client('s3')


#set the new bucket name
bucket = 'esthree01-2025'


#create a new bucket
client.create_bucket(Bucket=bucket)
print(f"bucket created successfully ")



# retrieve all bucket metadata

response = client.list_buckets()
#print(response)


#loop through bucket data and display bucket name
for b in response['Buckets']:
    print(b['Name'])
    
# Extract and print the owner details
owner_display_name = response['Owner']['DisplayName']
owner_id = response['Owner']['ID']

print(f"Bucket Owner: {owner_display_name} (ID: {owner_id})")