import json
import boto3
import os
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
  dynamodb = boto3.resource('dynamodb')
  table_name = os.environ.get('ORDERS_TABLE')
  table = dynamodb.Table(table_name)
  order_id = event['pathParameters']['id']
  path_params = event.get('pathParameters', {})
  order_id = path_params.get('id')

  try:
      order_id = int(order_id)
      response = table.query(KeyConditionExpression=Key('id').eq(order_id))

      return {
          "statusCode": 200,
          "body": response['Items']
      }

  except ValueError:
      return {
          "statusCode": 400,
          "body": "Invalid 'id' parameter. It must be a number."
      }

  except Exception as e:
      return {
          "statusCode": 500,
          "body": f"Internal server error: {str(e)}"
      }