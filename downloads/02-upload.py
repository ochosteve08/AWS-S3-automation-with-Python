import boto3
import os
from datetime import datetime

# Instantiate S3 client
client = boto3.client('s3')

# Set variables
bucket = 'esthree-2025'
cwr_path = os.path.dirname(os.path.abspath(__file__))  # Get current script's directory
file = 'report-lastyear.csv'
filename = os.path.join(cwr_path, '..', 'data', file)  # Move one level up and enter 'data'

# Ensure the file exists before attempting upload
if not os.path.exists(filename):
    print(f"Error: File '{filename}' not found!")
else:
    # Append timestamp to prevent overwriting in S3
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    new_filename = f"report-lastyear-{timestamp}.csv"

    # Upload the file
    client.upload_file(filename, bucket, new_filename)
    print(f"File uploaded successfully as {new_filename}!")
