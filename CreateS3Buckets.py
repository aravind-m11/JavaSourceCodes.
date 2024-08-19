import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    s3 = boto3.client('s3', region_name=region)
    
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f'Bucket {bucket_name} created successfully.')
    except ClientError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    # Example usage
    bucket_name = 'my-unique-bucket-name'
    region = 'us-west-1'  # Change this to your preferred region

    create_bucket(bucket_name, region)
