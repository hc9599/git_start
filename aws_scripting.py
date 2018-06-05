import boto3

ec2 = boto3.resource('ec2')
insstance = ec2.create_instances()