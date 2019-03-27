import json
import os
import logging


__author__ = "Romain CORNU"
__version__ = "0.1.0"


LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)


def lambda_handler(event, context):
    logging.info('Hello world')
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
