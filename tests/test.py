import unittest
from api.api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_score_endpoint(self):
        response = self.app.get('/score')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
