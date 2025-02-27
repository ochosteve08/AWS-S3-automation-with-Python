import boto3

# Instantiate S3 client
client = boto3.client('s3')

# Set variables
bucket = 'esthree-2025'
file = 'report-lastyear.csv'  # File to delete from S3

#list all objs in bucket
all_objs = client.list_objects(Bucket=bucket)
print(f'All objects in {bucket}: ')

for obj in all_objs['Contents']:
    print(obj['Key'], obj['LastModified'])

try:
    # Delete the file from S3
    response = client.delete_object(Bucket=bucket, Key=file)
    
    # Check if the delete was successful
    if response.get("ResponseMetadata", {}).get("HTTPStatusCode") == 204:
        print(f"✅ File '{file}' deleted successfully from '{bucket}'")
    else:
        print(f"⚠️ Deletion response: {response}")
except client.exceptions.ClientError as e:
    print(f"❌ Failed to delete file: {e}")
