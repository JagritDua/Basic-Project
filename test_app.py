import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello Hello Hello 7', response.data)

    def test_home2(self):
        response = self.app.get('/testing2')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'testing 2', response.data)

if __name__ == "__main__":
    unittest.main()
