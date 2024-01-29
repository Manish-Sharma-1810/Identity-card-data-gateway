############################## This is the main handler file of lambda function ##############################

import boto3
import json

import services
import database_connector as dbc

# for logging
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the main handler function for the lambda
def lambda_handler(event, context):
    logger.info('Lambda triggered!')

    # get bucket name and object key from the event record
    msg_obj = {
        'bucket_name': event['Records'][0]['s3']['bucket']['name'],
        'file_path': event['Records'][0]['s3']['object']['key'],
        'location': event['Records'][0]['awsRegion']
    }
    # get data
    data_obj = services.get_data_obj(msg_obj)
    # add data to dynamodb
    db_status = dbc.add_to_database(data_obj)
    
    return {
        "status_code": 200,
        "bucket_name": msg_obj['bucket_name'],
        "file_path": msg_obj['file_path'],
        "location": msg_obj['location'],
        "data": data_obj,
        "db_status": db_status
    }