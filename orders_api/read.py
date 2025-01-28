import json
import boto3
import os
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
  order = json.loads(event['body'])
  dynamodb = boto3.resource('dynamodb')
  table_name = os.environ.get('ORDERS_TABLE')
  table = dynamodb.Table(table_name)
  order_id = int(event['pathParameters']['id'])
  response = table.query(KeyConditionExpression=Key('id').eq(order_id))

  return {
    'statusCode': 200,
    'headers': {},
    'body': json.dumps(response['Items'])
  }