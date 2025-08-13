import boto3

s3 = boto3.client('s3')
bucket_name = 'trendytech-tutorial-bucket'
key = 'output/hello_world_output.txt'

s3.put_object(Bucket=bucket_name, Key=key, Body='Hello World from Glue!\n')