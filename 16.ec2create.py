import boto3

ec2=boto3.resource("ec2")

keyPairName="kash20" #key-0e38d373dc2a9837d
imageId="ami-0ed9277fb7eb570c9"

instances=ec2.create_instances(
    MinCount=2,
    MaxCount=3,
    ImageId=imageId,
    InstanceType="t2.micro",
    KeyName=keyPairName,
    TagSpecifications=[{
        "ResourceType":"instance",
        "Tags":[{
            "Key":"Name",
            "Value":"kash20"
        }]
    }]
)

for instance in instances:
    print("Instance Created with id as: ",instance.id)

    instance.wait_until_running()
    print("Started")