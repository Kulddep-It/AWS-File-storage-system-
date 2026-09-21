import boto3

s3 = boto3.client('s3')

def upload_file(file_name, bucket_name):
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Uploaded: {file_name}")

def list_files(bucket_name):
    response = s3.list_objects(Bucket=bucket_name)
    for file in response['Contents']:
        print(file['Key'])

def delete_file(bucket_name, file_name):
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    print(f"Deleted: {file_name}")
