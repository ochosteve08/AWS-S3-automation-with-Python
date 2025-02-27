import boto3

# instantiate a client
client = boto3.client('s3')


# retrieve all bucket metadata

response = client.list_buckets()
#print(response)


#loop through bucket data and display bucket name
for b in response['Buckets']:
    print(b['Name'])
    
# Extract and print the owner details
owner_display_name = response['Owner']['DisplayName']
owner_id = response['Owner']['ID']

print(f"Bucket Owner: {owner_display_name} (ID: {owner_id})")
