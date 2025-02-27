import boto3
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Instantiate S3 client
client = boto3.client('s3')

# Set the new bucket name
bucket = 'esthree02-2025'

# try:
#     # Create a new bucket
#     client.create_bucket(Bucket=bucket)
#     logging.info(f"Bucket '{bucket}' created successfully.")
# except client.exceptions.BucketAlreadyExists:
#     logging.warning(f"Bucket '{bucket}' already exists.")
# except client.exceptions.ClientError as e:
#     logging.error(f"Failed to create bucket: {e}")


def bucket_exists(bucket_name):
    try:
        client.head_bucket(Bucket=bucket_name)
        return True  # Bucket exists
    except client.exceptions.ClientError as e:
        # Check if the error is "Not Found" (404)
        if e.response['Error']['Code'] == '404':
            return False
        logging.error(f"Unexpected error checking bucket existence: {e}")
        return False

if bucket_exists(bucket):
    logging.info(f"Bucket '{bucket}' already exists.")
else:
    try:
        client.create_bucket(Bucket=bucket)
        logging.info(f"Bucket '{bucket}' created successfully.")
    except client.exceptions.ClientError as e:
        logging.error(f"Failed to create bucket: {e}")


# Retrieve all bucket metadata
try:
    response = client.list_buckets()
    
    # Extract and print the owner details
    owner_display_name = response.get('Owner', {}).get('DisplayName', 'N/A')
    owner_id = response.get('Owner', {}).get('ID', 'N/A')
    
    logging.info(f"Bucket Owner: {owner_display_name} (ID: {owner_id})")

    # Display all bucket names
    logging.info("Existing Buckets:")
    for b in response.get('Buckets', []):
        logging.info(f"- {b['Name']}")

except client.exceptions.ClientError as e:
    logging.error(f"Error retrieving bucket list: {e}")
