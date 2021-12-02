import boto3
import json


client = boto3.client('sts')

response =client.get_caller_identity()

userid=response['UserId']
account=response['Account']
arn=response['Arn']

output={
    "UserID" : userid,
    "Account" : account,
    "Arn" : arn
}

print(json.dumps(output,indent=4))