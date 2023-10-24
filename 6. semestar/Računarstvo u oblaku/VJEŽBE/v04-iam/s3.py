import boto3

localstack_access_key = 'test'
localstack_secret_key = 'test'
endpoint_url = 'http://localhost.localstack.cloud:4566'

aws_access_key = 'AKIAXRC7SALILG7HFMGS'
aws_secret_access_key = 'ni3MOAi0vjLaBOfim9P1DxqVW0'

session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_access_key
)

def hello_s3():
    # Creating high level object for interacting with S3 service
    # s3_client = session.client('s3')
    s3_client = session.client('s3', endpoint_url=endpoint_url)

    bucket_name = 'racunarstvo-u-oblaku-2023.example-bucket'

    # Creating S3 bucket
    print("=== Create bucket ===")
    bucket = s3_client.create_bucket(Bucket=bucket_name)
    
    # List all existing S3 buckets4
    print("=== List buckets ===")
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print(f"\t{bucket['Name']}")

    # Write object to bucket
    print("=== Write object to bucket ===")
    file_name = 'object.json'
    object_key = 'object1'
    s3_client.upload_file(file_name, bucket_name, object_key)

    # List all objects in bucket
    print("=== List all objects in bucket ===")
    response = s3_client.list_objects(Bucket=bucket_name)
    for o in response['Contents']:
        print(f"\t{o['Key']}")
    
    # Delete object
    print("=== Delete object from bucket ===")
    s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': [{'Key': object_key}]})

    # List all objects in bucket
    print("=== List all objects in bucket ===")
    response = s3_client.list_objects(Bucket=bucket_name)
    try:
        for o in response['Contents']:
            print(f"\t{o['Key']}")
    except (KeyError):
        print(f"\tNo content in bucket")

    # Delete bucket
    # print("=== Delete bucket ===")
    # s3_resource = session.resource('s3')
    # bucket = s3_resource.Bucket(bucket_name)
    # bucket.objects.all().delete()
    # bucket.delete()


if __name__ == '__main__':
    hello_s3()
