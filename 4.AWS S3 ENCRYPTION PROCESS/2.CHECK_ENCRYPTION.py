"""

# code to check encryption available or not
import boto3
#to grap the error we use to add exception
from botocore.exceptions import ClientError


def check_encryption():
    s3_client = boto3.client('s3')
#to get the bucket encryption
    try:
        response = s3_client.get_bucket_encryption(Bucket="parwizforogh-12")
        print(response)
# if not present to print
    except ClientError as e:
        print("No encryption is available in this bucket")



check_encryption()

#as of this code result we will get the information of encryption
"""
