import unittest
from app.main.index import index_page
from app import creat_app

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.app = creat_app()
        self.app.app_context()
        self.client = self.app.test_client()

    def testIndex(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'hello world!')
