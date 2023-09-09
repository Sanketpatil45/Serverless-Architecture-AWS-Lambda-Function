﻿import json 
import boto3
def lambda_handler(event, context):
ec2_connection=boto3. resource(service_name="ec2", region_name="ap-south-1")
filter_ec2tag={"Name": "tag: Env", "Values":["Test"]}
for each in ec2_connection.instances.filter(Filters=[filter_ec2tag]):
each.stop()
#each.start()

return {
'statusCode': 200,
'body' json.dumps ('Hello from Lambda!')
}
