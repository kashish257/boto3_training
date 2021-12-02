import boto3

resource=boto3.resource('ec2')
groupname="my vpc"
vpcid="vpc-0f99163c0bfce8255"
response= resource.create_security_group(
    Description="craeting sg",
    GroupName=groupname,
    VpcId=vpcid,
    TagSpecifications=[{
        "ResourceType":"security-group",
        "Tags":[{"Key":"Name",'Value':groupname}]
    }]
)

print(response.id)