import boto3


def get_aws():
    return boto3.resource('dynamodb',
                          aws_access_key_id='AKIARTLZHDAUXPP2SHMZ',
                          aws_secret_access_key='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',
                          region_name='eu-north-1')


def get_table_content():
    result = get_aws().Table('garden_temperature').scan()
    return result['Items']
