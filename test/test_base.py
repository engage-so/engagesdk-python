import unittest


class TestBase(unittest.TestCase):
    def build_url(self, url):
        return f'https://api.engage.so/v1{url}'