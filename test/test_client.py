import unittest

from engagesdk.engage import Engage
from engagesdk.error import EngageError


class ClientTest(unittest.TestCase):
    def test_client_error_no_keys(self):
        with self.assertRaises(EngageError) as context:
            engage = Engage(api_key='', secret_key='')
        self.assertTrue('Please pass valid API and Secret Key' in str(context.exception))
