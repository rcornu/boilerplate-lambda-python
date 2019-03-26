import json
import logging


__author__ = "Romain CORNU"
__version__ = "0.1.0"


logging.basicConfig(level=logging.DEBUG)


def lambda_handler(event, context):
    logging.info('Hello world')
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
