import boto3
import logging

logger =logging.getLogger()
logger.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(messages)s')

vpcclient=boto3.client('ec2')

def fnvpcdelete(vpcId):
    from botocore.exceptions import ClientError 
    vpc=None
    try:
        vpc=vpcclient.delete_vpc(Vpc_id=vpcId)
        logger.info("listing vpc")

    except ClientError as ce:
        print("found error",ce)
        logger.exception("not possible")
    return vpc

if __name__=="__main__":
    
    vpc=fnvpcdelete(vpcId="vpc-019568ee2d832946d")
    print("vpc")

