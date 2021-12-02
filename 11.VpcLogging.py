import boto3
import logging

logger =logging.getLogger()
#logger.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(messages)s')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

vpcclient=boto3.client('ec2',region_name="us-east-2")

def fnvpcdelete(vpcId):
    from botocore.exceptions import ClientError 
    vpc=None
    try:
        vpc=vpcclient.delete_vpc(VpcId=vpcId)
        logger.info("listing vpc")

    except ClientError as ce:
        print("found error",ce)
        logger.exception("not possible")
    return vpc

if __name__=="__main__":
    
    vpc=fnvpcdelete(vpcId="vpc-0ec3d57538331d1d1")
    print("vpc")

