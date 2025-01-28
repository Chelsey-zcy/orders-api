import json

def lambda_handler(event, context):
  order = json.loads(event['body'])
  return {
    'statusCode': 201,
    'headers': {},
    'body': json.dumps({'message': 'Order Created'})
  }