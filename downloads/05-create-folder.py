import boto3

# Instantiate S3 client
client = boto3.client('s3')

# Variables
target_bucket = 'esthree01-2025'
subfolder_1 = 'ec2-test/'
subfolder_2 = 'ecs-test/'   

# Create subfolders in the target bucket (S3 folders are just object keys with "/")
client.put_object(Bucket=target_bucket, Key=subfolder_1)  # Corrected Key parameter
client.put_object(Bucket=target_bucket, Key=subfolder_2)

# Retrieve object info from the bucket
response = client.list_objects(Bucket=target_bucket)

print("All objects in the bucket:")

# Check if 'Contents' exists to avoid errors when the bucket is empty
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("No objects found in the bucket.")
