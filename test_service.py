import requests
import db_connect
import json


def test_correctly_status_code():
    r = requests.get('http://127.0.0.1:5000/api/v1.0/users/1')
    assert r.status_code == 200


def test_content_type():
    r = requests.get('http://127.0.0.1:5000/api/v1.0/users/000001')
    assert r.headers['content-type'] == 'application/json'


def test_existing_user():
    r = requests.get('http://127.0.0.1:5000/api/v1.0/users/2')
    res_db = db_connect.db_executor(
        """SELECT full_name FROM users where id=%s""", (2,))
    json_data = json.loads(r.text)
    assert json_data['user'] == res_db[0]


def test_users():
    print('test_users')
    r = requests.get('http://127.0.0.1:5000/api/v1.0/users')
    json_data = json.loads(r.text)
    res_db = db_connect.db_executor("""SELECT * FROM users""")
    d = [tuple(i) for i in json_data['users']]
    assert d == res_db


def test_wrong_user():
    r = requests.get('http://127.0.0.1:5000/api/v1.0/users/1000')
    assert r.status_code == 404


def test_float_id():
    r = requests.get('http://127.0.0.1:5000/api/v1.0/users/0.1')
    assert r.status_code == 404


def test_string_id():
    print(123)
    r = requests.get('http://127.0.0.1:5000/api/v1.0/users/ch')
    assert r.status_code == 404
