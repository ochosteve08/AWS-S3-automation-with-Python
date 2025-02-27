import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Instantiate S3 client
client = boto3.client('s3')

# Variables
target_bucket = 'esthree02-2025'
subfolders = ['ec2-test/', 'ecs-test/']  # List of subfolders

try:
    # Create subfolders in the target bucket
    for subfolder in subfolders:
        client.put_object(Bucket=target_bucket, Key=subfolder)
        logging.info(f"Created subfolder: {subfolder}")

    # Retrieve object info from the bucket
    response = client.list_objects_v2(Bucket=target_bucket)  # Use list_objects_v2 (better performance)

    logging.info("All objects in the bucket:")

    # Check if 'Contents' exists to avoid errors when the bucket is empty
    if 'Contents' in response:
        for obj in response['Contents']:
            logging.info(f"- {obj['Key']}")
    else:
        logging.info("No objects found in the bucket.")

except client.exceptions.ClientError as e:
    logging.error(f"AWS Client Error: {e}")
except Exception as e:
    logging.error(f"An error occurred: {e}")
