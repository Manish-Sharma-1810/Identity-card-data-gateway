############################## This is the main handler file of lambda function ##############################

import database_connector as dbc

# for logging
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the main handler function for lambda
def lambda_handler(event, context):
    logger.info("Lambda triggered!")
    httpMethod = event['httpMethod']
    path = event['path']

    if httpMethod == 'GET' and path == '/info':
        response = dbc.get_info(event['queryStringParameters']['id'])
    else:
        response = dbc.build_response(404, "Not Found!")
    return response
