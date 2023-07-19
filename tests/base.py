import unittest
from client import Client

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        proxies = {
            'http': 'socks5h://127.0.0.1:27020',
            'https': 'socks5h://127.0.0.1:27020'
        }
        cls.client = Client(proxies=proxies)


    @classmethod
    def tearDownClass(cls):
        del cls.client
