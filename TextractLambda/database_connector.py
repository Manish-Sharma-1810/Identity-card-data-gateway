###################### This file is reponsible for the database related services ######################

import boto3
from botocore.exceptions import ClientError

# for logging
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create an object for dynamodb and get the table from dynamodb
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('adhar-data-table')

# Define the function for check an item into the database
def is_present(id):
    try:
        response = table.get_item(
            Key = {
                "id": id,
            }
        )
        result = response["Item"]
    except (Exception, ClientError) as e:
        print(f'ERROR: {e}!')
        result = None

    if result is not None:
        return True
    else:
        return False

# Define a function to add new entries to the database
def add_to_database(obj):
    logger.info("adding to database ...")
    is_present = is_present(ID=obj["id"])

    if is_present:
        report = "Record already present in database"
    else:
        # Add item to the database
        try:
            table.put_item(Item=obj)
            report = "Record successfully added to database"
        except (Exception, ClientError) as e:
            print(f'ERROR: {e}!')
            report = "Record failed to add to database"
    return report