"""

# delete encryption from a bucket
import boto3


def delete_encryption():
# creating client
    s3_client = boto3.client('s3')
# delete bucket encryption
    response = s3_client.delete_bucket_encryption(Bucket='parwizforogh-12')
    print(response)



delete_encryption()
"""
