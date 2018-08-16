import boto3

def run_from_lambda(event, context):
    ecs = boto3.client('ecs')
    response = ecs.run_task(
        cluster='wonka',
        launchType='FARGATE',
        taskDefinition='counttothree:1',
        count=1
        platformVersion='LATEST',
    )

    return str(response)
