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
        print(f"\n❌ Error deleting bucket '{bucket_name}': {e}")

# Step 1: List all S3 buckets
buckets = list_buckets()
if not buckets:
    print("\n⚠️ No S3 buckets found.")
    exit()

print("\n📂 Available S3 Buckets:")
for i, bucket in enumerate(buckets, 1):
    print(f"{i}. {bucket}")

# Step 2: Select multiple buckets to delete (comma-separated input)
bucket_indices = input("\nEnter the numbers of the buckets to delete (comma-separated, e.g., 1,3,5): ")
selected_indices = [int(i.strip()) for i in bucket_indices.split(',') if i.strip().isdigit() and 1 <= int(i.strip()) <= len(buckets)]

if not selected_indices:
    print("\n❌ Invalid bucket selection.")
    exit()

selected_buckets = [buckets[i - 1] for i in selected_indices]
print(f"\n🚨 Selected buckets: {', '.join(selected_buckets)}")

# Step 3: Confirm deletion
confirm = input(f"\n⚠️ Are you sure you want to delete the following buckets? {', '.join(selected_buckets)} (yes/no): ").strip().lower()
if confirm != "yes":
    print("\n✅ Bucket deletion canceled.")
    exit()

# Step 4: Delete all objects and buckets
for bucket_name in selected_buckets:
    delete_all_objects(bucket_name)
    delete_bucket(bucket_name)

# Step 5: Show remaining buckets
buckets = list_buckets()
if buckets:
    print("\n📂 Remaining S3 Buckets:")
    for bucket in buckets:
        print(f"- {bucket}")
else:
    print("\n🗑️ No S3 buckets left.")



