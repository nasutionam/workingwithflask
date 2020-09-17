import boto3
import json
from botocore.exceptions import ClientError

secret_name = "di_pay"
region_name = "eu-west-1"

session = boto3.session.Session()

client = session.client(
    service_name='secretsmanager',
    region_name=region_name,
)

try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        print("The requested secret " + secret_name + " was not found")
    elif e.response['Error']['Code'] == 'InvalidRequestException':
        print("The request was invalid due to:", e)
    elif e.response['Error']['Code'] == 'InvalidParameterException':
        print("The request had invalid params:", e)
else:
    if 'SecretString' in get_secret_value_response:
        secret = json.loads(get_secret_value_response['SecretString'])
    else:
        binary_secret_data = get_secret_value_response['SecretBinary']

dbendpoint = secret['dbendpoint']
dbuser = secret['dbuser']
dbpass = secret['dbpass']
dbport = secret['dbport']

print(dbendpoint)
print(dbuser)
print(dbpass)
print(dbport)