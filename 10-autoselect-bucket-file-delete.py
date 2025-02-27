import boto3

# Instantiate S3 client
client = boto3.client('s3')

# Function to list all buckets
def list_buckets():
    response = client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

# Function to list files in a bucket
def list_files(bucket_name):
    response = client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    return []

# Step 1: List and select an S3 bucket
buckets = list_buckets()
if not buckets:
    print("\n⚠️ No S3 buckets found.")
    exit()

print("\n📂 Available S3 Buckets:")
for i, bucket in enumerate(buckets, 1):
    print(f"{i}. {bucket}")

bucket_index = input("\nEnter the number of the bucket to use: ")
if not bucket_index.strip().isdigit() or not (1 <= int(bucket_index) <= len(buckets)):
    print("\n❌ Invalid bucket selection.")
    exit()

bucket_name = buckets[int(bucket_index) - 1]
print(f"\n✅ Selected bucket: {bucket_name}")

# Step 2: List files in the selected bucket
files = list_files(bucket_name)

if not files:
    print("\n⚠️ No files found in the bucket.")
    exit()

print("\n📂 Files in bucket:")
for i, file in enumerate(files, 1):
    print(f"{i}. {file}")

# Step 3: Select files for deletion
indices = input("\nEnter the file numbers to delete (comma-separated): ")
selected_files = [files[int(i) - 1] for i in indices.split(",") if i.strip().isdigit() and 0 < int(i) <= len(files)]

if not selected_files:
    print("\n⚠️ No valid files selected.")
    exit()

# Step 4: Delete selected files
objects = [{'Key': file} for file in selected_files]
client.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})
print(f"\n✅ Deleted files: {selected_files}")

# Step 5: List remaining files
remaining_files = list_files(bucket_name)
if remaining_files:
    print("\n📂 Files left in bucket:")
    for file in remaining_files:
        print(f"- {file}")
else:
    print("\n🗑️ The bucket is now empty.")
