# Identity-card-data-gateway
Identity-card-data-gateway: A serverless project leveraging AWS Lambda, Textract, DynamoDB, S3, and API Gateway for extracting and managing identity card data with ease and efficiency.

Identity-card-data-gateway is a serverless solution designed to extract, manage, and provide access to essential information from identity cards. It leverages AWS Lambda, Amazon Textract, DynamoDB, S3, and API Gateway to streamline the process of extracting data from uploaded identity cards, storing it securely, and enabling easy access through a RESTful API.

## Table of Contents

- [Usecase](#usecase)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Usecase

The primary use case for Identity-card-data-gateway is to facilitate the extraction and management of key information from identity cards. Users can upload their identity cards to an S3 bucket in (.jpeg, .jpg, or .png formats only), which triggers a Lambda function to extract data such as ID number, date of birth, name, and more using Amazon Textract. The extracted data is then stored securely in DynamoDB. Through integration with API Gateway, users can access their extracted card data via a RESTful API, enabling seamless integration with various applications and services.

## Technologies Used

- **AWS Lambda**: For serverless computing to execute the extraction and storage processes.
- **Amazon Textract**: Utilized for extracting text and data from uploaded identity cards.
- **DynamoDB**: NoSQL database used for storing extracted card data securely.
- **S3**: Amazon Simple Storage Service for storing uploaded identity cards.
- **API Gateway**: For creating RESTful APIs to access extracted card data.

## Setup Instructions

1. **AWS Account**: Ensure you have an AWS account set up with appropriate permissions for Lambda, Textract, DynamoDB, S3, and API Gateway.
2. **Configuration**: Set up your AWS credentials and configure your AWS services accordingly.
3. **Deployment**: Deploy the Lambda functions, set up triggers for S3 events, create DynamoDB tables, and configure API Gateway endpoints.
4. **Permissions**: Configure IAM roles and permissions for accessing AWS resources securely.
5. **Environment Variables**: Set any necessary environment variables for your Lambda functions or API Gateway endpoints.

## Usage

1. **Upload Identity Cards**: Users can upload their identity cards to the designated S3 bucket.
2. **Extraction Process**: Upon upload, the system triggers a Lambda function to extract data using Amazon Textract.
3. **Data Storage**: Extracted card data is securely stored in DynamoDB for easy retrieval and management.
4. **API Access**: Users can access their extracted card data through API Gateway endpoints.

## Contributing

Contributions to Identity-card-data-gateway are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
