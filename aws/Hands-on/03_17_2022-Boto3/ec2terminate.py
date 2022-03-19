import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-06d01c8cca27a300f').terminate()