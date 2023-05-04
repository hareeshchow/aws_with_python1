"""

# get the policy encryption from bucket
import boto3

s3_client = boto3.client('s3')
#----syntax-->get_bucket_policy (Bucket='bucketname')-----syntax
response = s3_client.get_bucket_policy(Bucket='parwizforogh-12')
print(response['Policy'])
"""
