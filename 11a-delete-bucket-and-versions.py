import boto3

# Instantiate S3 client
client = boto3.client('s3')

# Function to list all buckets
def list_buckets():
    response = client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

# Function to list all object versions (not just current versions)
def list_object_versions(bucket_name):
    response = client.list_object_versions(Bucket=bucket_name)
    versions = response.get('Versions', []) + response.get('DeleteMarkers', [])
    return [{'Key': obj['Key'], 'VersionId': obj['VersionId']} for obj in versions]

# Function to delete all objects (including all versions and delete markers)
def delete_all_objects(bucket_name):
    objects = list_object_versions(bucket_name)
    if not objects:
        print(f"\n✅ Bucket '{bucket_name}' is already empty.")
        return

    delete_list = [{'Key': obj['Key'], 'VersionId': obj['VersionId']} for obj in objects]
    client.delete_objects(Bucket=bucket_name, Delete={'Objects': delete_list})
    print(f"\n🗑️ Deleted ALL versions of objects in bucket: {bucket_name}")

# Function to delete the bucket
def delete_bucket(bucket_name):
    try:
        client.delete_bucket(Bucket=bucket_name)
        print(f"\n✅ Bucket '{bucket_name}' has been deleted successfully.")
    except client.exceptions.ClientError as e:
        print(f"\n❌ Error deleting bucket: {e}")

# Step 1: List all S3 buckets
buckets = list_buckets()
if not buckets:
    print("\n⚠️ No S3 buckets found.")
    exit()

print("\n📂 Available S3 Buckets:")
for i, bucket in enumerate(buckets, 1):
    print(f"{i}. {bucket}")

# Step 2: Select a bucket to delete
bucket_index = input("\nEnter the number of the bucket to delete: ")
if not bucket_index.strip().isdigit() or not (1 <= int(bucket_index) <= len(buckets)):
    print("\n❌ Invalid bucket selection.")
    exit()

bucket_name = buckets[int(bucket_index) - 1]
print(f"\n🚨 Selected bucket: {bucket_name}")

# Step 3: Delete all object versions
delete_all_objects(bucket_name)

# Step 4: Confirm final deletion
confirm = input(f"\n⚠️ Are you sure you want to delete bucket '{bucket_name}'? (yes/no): ").strip().lower()
if confirm != "yes":
    print("\n✅ Bucket deletion canceled.")
    exit()

# Step 5: Delete the bucket
delete_bucket(bucket_name)

# Step 6: Show remaining buckets
buckets = list_buckets()
if buckets:
    print("\n📂 Remaining S3 Buckets:")
    for bucket in buckets:
        print(f"- {bucket}")
else:
    print("\n🗑️ No S3 buckets left.")
