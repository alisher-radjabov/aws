import json
import boto3

# boto3 S3 init
s3_client = boto3.client("s3")

def lambda_handler(event, context):
   destinationBucketName = 'YourDestinationBuckeName'

   # event containing info about uploaded object
   print("Event :", event)

   # Bucket Name where file was uploaded
   sourceBucketName = event['Records'][0]['s3']['bucket']['name']

   # Filename of object (with path)
   fileKeyName = event['Records'][0]['s3']['object']['key']

   # Copy Source Object
   copySourceObject = {'Bucket': sourceBucketName, 'Key': fileKeyName}

   # S3 copy object operation
   s3_client.copy_object(CopySource=copySourceObject, Bucket=destinationBucketName, Key=fileKeyName)

   return {
       'statusCode': 200,
       'body': json.dumps('Object uploaded successfully to your s3 bucket!')
   }