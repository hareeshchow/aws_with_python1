import boto3


user_data_script = """
#!/bin/bash
yum update -y 
yum install -y httpd
chkconfig httpd on
service httpd start
echo "<h1>Welcome to Python & Boto3 Course</h1>" > /var/www/html/index.html

"""

ec2_resource = boto3.resource('ec2')

response = ec2_resource.create_instances(
    ImageId='ami-0b0dcb5067f052a63',
    MinCount= 1,
    MaxCount  =1,
    InstanceType='t2.micro',
    KeyName='mykey',
    SecurityGroups=[
        'launch-wizard-1'
    ],
    UserData = user_data_script
)

print(response)
