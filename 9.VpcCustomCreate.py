import boto3
def fncreatedefaultvpc(vpcresorces,ip_cidr):
    from botocore.exceptions import ClientError
    vpcId="Not set"
    try:
        response=vpcresorces.create_vpc(CidrBlock=ip_cidr,
        InstanceTenancy='default',
        TagSpecifications=[{"ResourceType":"vpc","Tags":[{"Key" : "Name","Value" : "kashish45"}]}]
            )
        vpcId=response.id
        print("created default vpc")
    except ClientError as ce:
        print("not possible",ce)
    return vpcId


if __name__=="__main__":
    vpcresorces=boto3.resource("ec2",region_name="us-east-2")
    ip_cidr="192.168.0.0/26"
    vpcId=fncreatedefaultvpc(vpcresorces,ip_cidr)
    print(vpcId)