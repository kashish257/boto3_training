import boto3

client =boto3.client("s3")
# bucketName="botobucktkashish"
# response=client.list_buckets()
# for b in response["Buckets"]:
#     if( "bkt" in b["Name"]):
#         #print()
#         print(b["Name"])


resource=boto3.resource('s3')
it=resource.buckets.all()

for b in it:
    print(f"----{b.name}")