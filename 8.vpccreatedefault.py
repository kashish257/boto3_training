import boto3
def fncreatedefaultvpc(vpcClient):
    from botocore.exceptions import ClientError
    try:
        response=vpcClient.create_default_vpc()
        vpcId=response["Vpc"]["VpcId"]
        print("created default vpc")
    except ClientError:
        print("not possible")


#drive code

if __name__=="__main__":
    vpcclient=boto3.client("ec2")
    vpcId=fncreatedefaultvpc(vpcclient)
    print(vpcId)




