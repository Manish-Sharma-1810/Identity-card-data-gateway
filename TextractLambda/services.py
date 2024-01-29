################################ This file is responsible for providing general tools and services ################################

import re
import boto3
from botocore.exceptions import ClientError

# for logging
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the function for cleaning the id
def clean_id(id):
    cleaned_id = id.replace('-', '').replace('.', '').replace('!', '').replace('?', '').replace(',', '').replace(' ', '')
    return cleaned_id

# Define the function for cleaning the Gender
def clean_gender(gender):
    sex = gender.replace('-', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(',', ' ').replace('/', ' ').lower()
    if "female" in sex:
        return "female"
    elif "male" in sex:
        return "male"
    else:
        return "nan"

# Define the function for cleaning the DOB
def clean_dob(dob):
    l1 = dob.replace('/', '-')
    rgx = r'\d{2}-\d{2}-\d{4}'
    l2 = re.search(rgx, l1)[0]
    return l2

# Define the function for getting Name, DOB, gender, ID
def get_data_obj(text_lines):
    name = text_lines[3]
    dob = clean_dob(text_lines[4])
    gender = clean_gender(text_lines[5])
    id = clean_id(text_lines[6])
    data_obj = {
        "id": id,
        "name": name,
        "dob": dob,
        "gender":gender
    }
    return data_obj

# Define the function for extracting the line text from the textract response.
def get_text_lines(textract_response):
    logger.info("getting text lines from textract_response ...")
    outliers = ['-']

    # iterate each block of the response and store the line text into a list
    line_text_list = []
    for block in response["Blocks"]:
        if (block["BlockType"] == "LINE") and (block["Text"] not in outliers):
            line_text_list.append(block["Text"])
    return line_text_list

# Define the function to extract the plain text from the image
def get_textract_response(msg_obj):
    logger.info('extracting the plain text ...')
    textract_client = boto3.client('textract', region_name=msg_obj['location'])
    try:
        response = textract_client.detect_document_text(
                Document={
                    "S3Object": {
                        "Bucket": msg_obj['bucket_name'],
                        "Name": msg_obj['file_path']
                    }
                }
            )
        return response
    except (Exception, ClientError) as e:
        print(f'ERROR: {e}!')
        return None

# Define the function to get data
def get_data_from_image(msg_obj):
    textract_response = get_textract_response(msg_obj)
    data_obj = None

    if textract_response is not None:
        text_lines = get_text_lines(textract_response)

        if len(text_lines) > 1:
            data_obj = get_data_obj(text_lines)

    return data_obj