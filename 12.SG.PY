import boto3

vpcResource=boto3.resource("ec2",region_name="us-east-2")

groupName="sgsamplebasicusage"
vpcId="vpc-06ebea409edc3078c"

response=vpcResource.create_security_group(
    Description="creating for demo purpose",
    GroupName=groupName,
    VpcId=vpcId,
    TagSpecifications=[{
        "ResourceType":"security-group",
        "Tags":[{'Key':'Name','Value':groupName}]
    }]
    )

print(response.id) #sg-06c6dc520c80cbc48