import boto3

# Instantiate S3 client
client = boto3.client('s3')

# Function to list all buckets
def list_buckets():
    response = client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

# Function to list all objects (including folders) in a bucket
def list_objects(bucket_name):
    response = client.list_objects_v2(Bucket=bucket_name)
    return [obj['Key'] for obj in response.get('Contents', [])]  # Includes folders (prefixes)

# Function to delete all objects (including folders) in a bucket
def delete_all_objects(bucket_name):
    objects = list_objects(bucket_name)
    if not objects:
        return
    delete_list = [{'Key': obj} for obj in objects]  # Folders are treated as keys too
    client.delete_objects(Bucket=bucket_name, Delete={'Objects': delete_list})
    print(f"\n🗑️ Deleted all objects (including folders) in bucket: {bucket_name}")

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

# Step 3: Check if bucket has objects and delete them
objects = list_objects(bucket_name)
if objects:
    print(f"\n⚠️ The bucket '{bucket_name}' is NOT empty. It contains {len(objects)} objects (including folders).")
    confirm_objects = input("Do you want to delete all objects inside it? (yes/no): ").strip().lower()
    if confirm_objects != "yes":
        print("\n✅ Bucket deletion canceled.")
        exit()

    delete_all_objects(bucket_name)

# Step 4: Confirm final deletion
confirm = input(f"\n⚠️ Are you sure you want to delete bucket '{bucket_name}'? (yes/no): ").strip().lower()
if confirm != "yes":
    print("\n✅ Bucket deletion canceled.")
    exit()

# Step 5: Delete the bucket
try:
    client.delete_bucket(Bucket=bucket_name)
    print(f"\n✅ Bucket '{bucket_name}' has been deleted successfully.")
except client.exceptions.ClientError as e:
    print(f"\n❌ Error deleting bucket: {e}")

# Step 6: Show remaining buckets
buckets = list_buckets()
if buckets:
    print("\n📂 Remaining S3 Buckets:")
    for bucket in buckets:
        print(f"- {bucket}")
else:
    print("\n🗑️ No S3 buckets left.")
