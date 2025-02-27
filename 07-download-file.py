import os
import boto3


# Instantiate S3 client
client = boto3.client('s3')

# Set variables
bucket = 'esthree-2025'
curr_path = os.path.dirname(os.path.abspath(__file__))  # Get current script's directory
# curr_path = os.getcwd() # Get current working directory

# os.makedirs(cwr_path, exist_ok=True)
file = 'report-lastyear.csv'
filename = os.path.join(curr_path, 'download', file)  

print(f"Downloading file to: {filename}")


    # object method to download file
    
try:
    # Download the file from S3
    client.download_file(Bucket=bucket, Key=file, Filename=filename)
    print(f"File downloaded successfully to: {filename}")
except client.exceptions.NoSuchKey:
    print(f"Error: File '{file}' not found in bucket '{bucket}'.")
except client.exceptions.ClientError as e:
    print(f"Failed to download file: {e}")



#list the contents of DL dir


download_dir = os.path.join(curr_path, 'download')
for root, dirs, files in os.walk(download_dir):
    for fn in files:
        print(fn)
