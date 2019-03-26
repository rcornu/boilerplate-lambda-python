import json
import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))  # noqa: E501
import lambda_function as function  # noqa: E402


class TestSample(unittest.TestCase):
    def test_sample_function(self):
        result = function.lambda_handler(None, None)
        self.assertEqual(result, {
            'statusCode': 200,
            'body': json.dumps('OK')
        })


if __name__ == '__main__':
    unittest.main()
