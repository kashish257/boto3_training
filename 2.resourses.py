import boto3

resource =boto3.resource("iam")

for r in resource.roles.all():
    print(r.name)

