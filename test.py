import unittest
import json
from main import app  # Import the Flask app from your app.py


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        data = response.data.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 'Hello, World!')

    def test_add_item(self):
        data = {'username': 'user1', 'item': 'item1'}
        response = self.app.post('/add_item', data=json.dumps(data), content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['username'], 'user1')
        self.assertEqual(response_data['message'], 'item1')

    def test_view_items(self):
        username = 'user1'
        response = self.app.get(f'/view_items/{username}')
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['username'], 'user1')
        self.assertEqual(response_data['message'], [])

    def test_delete_item(self):
        username = 'user1'
        index = 1
        response = self.app.delete(f'/delete_item/{username}/{index}')
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['username'], 'user1')
        self.assertEqual(response_data['message'], 'deleted: item1')


if __name__ == '__main__':
    unittest.main()
