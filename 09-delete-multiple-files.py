import boto3

# Instantiate S3 client
client = boto3.client('s3')

# Set bucket name
bucket = 'esthree-2025'

# Function to list files in the bucket
def list_files():
    response = client.list_objects_v2(Bucket=bucket)
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    return []

try:
    # 1. List all files before deletion
    files = list_files()

    if files:
        print("\n📂 Files in bucket:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")

        # 2: Get user selection
        indices = input("\nEnter the file numbers to delete (comma-separated): ")
        selected_files = [files[int(i) - 1] for i in indices.split(",") if i.strip().isdigit() and 0 < int(i) <= len(files)]

        if selected_files:
            # Prepare objects for deletion
            objects = [{'Key': file} for file in selected_files]

            # Delete the selected files
            client.delete_objects(Bucket=bucket, Delete={'Objects': objects})
            print(f"\n✅ Deleted files: {selected_files}")

        else:
            print("\n⚠️ No valid files selected.")

    else:
        print("\n⚠️ No files found in the bucket.")

except client.exceptions.ClientError as e:
    print(f"\n❌ Error: {e}")

# 3: List remaining files
remaining_files = list_files()
if remaining_files:
    print("\n📂 Files left in bucket:")
    for file in remaining_files:
        print(f"- {file}")
else:
    print("\n🗑️ The bucket is now empty.")
# This script demonstrates how to delete multiple files from an S3 bucket. It first lists all files in the bucket, then prompts the user to select files for deletion. The selected files are then deleted, and the remaining files are listed.