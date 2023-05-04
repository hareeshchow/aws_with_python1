"""

# encryption disable to enable using python
import boto3

def set_encryption():
    # create s3 clients
    s3_client = boto3.client('s3')
    # creating responce
    responce = s3_client.put_bucket_encryption(
        # need to give the bucket name
        Bucket='owmname',
        # need to specify the type of encryption
        ServerSideEncryptionConfigaration={
            # addind the rule here we need to use algorithm
            "Rules": [
                {"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        }
    )

    print(response)


set_encryption()

        }
    )

"""
