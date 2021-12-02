import boto3




resource=boto3.resource('s3')
bucket=resource.Bucket("botobucket")
bucket.delete()
Print("deleted")

