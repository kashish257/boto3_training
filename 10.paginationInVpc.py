import boto3
vpcclient=boto3.client('ec2')
def fnVpcdescribe(tagKey,tagValues,maxItems=5):    
    from botocore.exceptions import ClientError    
    vpcLists=[]
    try:        
        paginator=vpcclient.get_paginator("describe_vpc")
        response_iterator=paginator.paginate(Filters=[
        {
            'Name':f"tag:{tagKey}",
            "Values" : tagValues

        }
        ],PaginationConfig={'MaxItems':maxItems})
        Full_result=response_iterator.build_full_result()
        for i in Full_result["Vpcs"]:
            vpcLists.append(i)
        print("listing Vpc")

    except ClientError as ce:
        print("Error",ce)
    return vpcLists


if __name__=="__main__":
    
    vpclists=fnVpcdescribe(tagKey="Name",tagValues=["kashish","kash"],maxItems=10)
    for vpc in vpclists:
        print(vpc)