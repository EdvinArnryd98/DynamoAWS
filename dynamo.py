import boto3


def get_aws():
    return boto3.resource('dynamodb',
                          aws_access_key_id='',
                          aws_secret_access_key='',
                          region_name='eu-north-1')


def get_table_content():
    result = get_aws().Table('garden_temperature').scan()
    return result['Items']
