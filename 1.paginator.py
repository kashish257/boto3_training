import boto3

client = boto3.client('iam')

paginator =client.get_paginator('list_roles')

#print(paginator)

for page in paginator.paginate():
    #print("page" ,page)
    
    for r in page['Roles']:
        print("Role name :",r['RoleName'])
     


