import boto3

# Instantiate S3 client
client = boto3.client('s3')

# Function to list all S3 buckets
def list_buckets():
    response = client.list_buckets()
    return [bucket['Name'] for bucket in response.get('Buckets', [])]

# Function to list folders (prefixes) in an S3 bucket
def list_folders(bucket_name):
    response = client.list_objects_v2(Bucket=bucket_name, Delimiter='/')
    return [prefix['Prefix'] for prefix in response.get('CommonPrefixes', [])] if 'CommonPrefixes' in response else []

# Function to delete all objects inside selected folders
def delete_folders(bucket_name, folder_names):
    objects = []
    for folder in folder_names:
        # Fetch all objects within the folder
        response = client.list_objects_v2(Bucket=bucket_name, Prefix=folder)
        if 'Contents' in response:
            objects.extend([{'Key': obj['Key']} for obj in response['Contents']])

    if objects:
        # Delete objects
        client.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})
        print(f"\n🗑️ Deleted folders: {', '.join(folder_names)} and their contents.")
    else:
        print("\n⚠️ Selected folders were already empty.")

# Function to check if a folder is empty
def is_folder_empty(bucket_name, folder_name):
    response = client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
    return 'Contents' not in response  # If 'Contents' is missing, the folder is empty

# Step 1: List all S3 buckets
buckets = list_buckets()

if not buckets:
    print("\n⚠️ No buckets found in your AWS account.")
    exit()

print("\n📦 Available S3 Buckets:")
for i, bucket in enumerate(buckets, 1):
    print(f"{i}. {bucket}")

# Step 2: Select a bucket
bucket_index = input("\nEnter the number of the bucket to manage: ").strip()

if not bucket_index.isdigit() or not (1 <= int(bucket_index) <= len(buckets)):
    print("\n❌ Invalid bucket selection.")
    exit()

bucket_name = buckets[int(bucket_index) - 1]
print(f"\n🚀 Selected bucket: {bucket_name}")

# Step 3: List folders inside the bucket
folders = list_folders(bucket_name)

if not folders:
    print("\n⚠️ No folders found in the selected bucket.")
    exit()

print("\n📂 Available folders in the bucket:")
for i, folder in enumerate(folders, 1):
    print(f"{i}. {folder}")

# Step 4: Select folders to delete
folder_indices = input("\nEnter the numbers of the folders to delete (comma-separated): ")
selected_folders = [folders[int(i.strip()) - 1] for i in folder_indices.split(",") if i.strip().isdigit() and 0 < int(i.strip()) <= len(folders)]

if not selected_folders:
    print("\n❌ No valid folders selected.")
    exit()

print(f"\n🚨 Selected folders: {', '.join(selected_folders)}")

# Step 5: Confirm deletion
confirm = input(f"\n⚠️ Are you sure you want to delete these folders? (yes/no): ").strip().lower()
if confirm != "yes":
    print("\n✅ Folder deletion canceled.")
    exit()

# Step 6: Delete the folders
delete_folders(bucket_name, selected_folders)

# Step 7: Remove empty folder markers (optional)
for folder in selected_folders:
    if is_folder_empty(bucket_name, folder):  # Ensure the folder is empty before attempting deletion
        client.delete_object(Bucket=bucket_name, Key=folder)
        print(f"📂 Empty folder marker removed: {folder}")

print("\n✅ Folder deletion completed.")
