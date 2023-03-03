import boto3

ddb = boto3.resource("dynamodb")
table = ddb.Table('Emergency')

def lambda_handler(event, context):
    #Adding the emergency to the DynamoDB table
    table.put_item(Item=event)

    #Get all the emergencies that have been reported
    emergencies = table.scan()['Items']

    return emergencies

 
 
