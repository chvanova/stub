import requests
import unittest
import db_connect
import json


class TestService(unittest.TestCase):

    def test_correctly_status_code(self):
        r = requests.get('http://127.0.0.1:5000/api/v1.0/users/1')
        self.assertEqual(r.status_code, 200)

    def test_content_type(self):
        r = requests.get('http://127.0.0.1:5000/api/v1.0/users/000001')
        self.assertEqual(r.headers['content-type'], 'application/json')

    def test_existing_user(self):
        r = requests.get('http://127.0.0.1:5000/api/v1.0/users/2')
        res_db = db_connect.db_executor(
            """SELECT full_name FROM users where id=%s""", (2,))
        json_data = json.loads(r.text)
        self.assertEqual(json_data['user'], res_db[0])

    def test_users(self):
        r = requests.get('http://127.0.0.1:5000/api/v1.0/users')
        json_data = json.loads(r.text)
        res_db = db_connect.db_executor("""SELECT * FROM users""")
        d = [tuple(i) for i in json_data['users']]
        self.assertEqual(d, res_db)

    def test_wrong_user(self):
        r = requests.get('http://127.0.0.1:5000/api/v1.0/users/1000')
        self.assertEqual(r.status_code, 404)

    def test_float_id(self):
        r = requests.get('http://127.0.0.1:5000/api/v1.0/users/0.1')
        self.assertEqual(r.status_code, 404)

    def test_string_id(self):
        r = requests.get('http://127.0.0.1:5000/api/v1.0/users/ch')
        self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()