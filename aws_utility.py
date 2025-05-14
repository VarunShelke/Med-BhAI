import boto3


def initialize_bedrock_client():
    session = boto3.session.Session()
    bedrock = session.client(service_name='bedrock-runtime', region_name='us-east-1')

    return bedrock
