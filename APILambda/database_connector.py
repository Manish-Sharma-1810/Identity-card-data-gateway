###################### This file is reponsible for the database related services ######################

import json
import boto3
from botocore.exceptions import ClientError

# create an object for dynamodb and get the table from dynamodb
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('aadhar-data-table')

# Define the function for building the response in json
def build_response(status_code, body=None):
    response = {
        "status_code": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",

        }
    }
    if body is not None:
        response["body"] = json.dumps(body)
    return response

# Define the function for getting info from adhar id
def get_info(aadhar_id):
    try:
        response = table.get_item(
            Key = {
                "id": aadhar_id,
            }
        )
        if 'Item' in response:
            return build_response(200, response['Item'])
        else:
            return build_response(404, {'Message': 'AdharID: %s not found!' % aadhar_id})
    except (Exception, ClientError) as e:
        print(f'ERROR: {e}')
        return build_response(502, {'Message': 'Internal Server Error!'})