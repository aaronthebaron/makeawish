import sys
import boto3

QUEUE_NAME = 'wishes'

sqs = boto3.client('sqs')

response = sqs.create_queue( QueueName=QUEUE_NAME, Attributes={ 'DelaySeconds': '60', 'MessageRetentionPeriod': '86400' })
if response['ResponseMetadata']['HTTPStatusCode'] != 200:
    print('Could not get or create a queue')
    sys.exit(1)

queue_url = response['QueueUrl']

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=0,
    MessageBody=(
        'Hold Your Breath'
        'Make A Wish'
        'Count To Three'
    )
)
