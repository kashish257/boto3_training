import boto3
#
# import os

client =boto3.client("s3")
#AWS_REGION=os.environ["RC"]

bucketName="botobucktkashish"


response=client.create_bucket(Bucket=bucketName)
# ,CreateBucketConfiguration=location)
print("check with: aws s3 ls")