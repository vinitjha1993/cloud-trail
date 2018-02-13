import boto3
from botocore.client import Config

client = boto3.client('cloudtrail')

# create_trail
response = client.create_trail(
    Name='r_v_trail',
    S3BucketName='cloudtraillogsrv',
    IncludeGlobalServiceEvents=False,
    IsMultiRegionTrail=False,
    EnableLogFileValidation=False,

)

res = client.start_logging(
    Name='arn:aws:cloudtrail:us-west-2:649347328056:trail/r_v_trail'
)