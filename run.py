from flask import Flask, jsonify
from flask import abort
from flask import make_response
from db_connect import db_executor

app = Flask(__name__)


@app.route('/api/v1.0/users', methods=['GET'])
def get_users():
    select_users = """SELECT * FROM users"""
    users = db_executor(select_users)
    # print(users)
    return jsonify({'users': users})


@app.route('/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    select_by_id = """SELECT full_name FROM users where id=%s"""
    user = db_executor(select_by_id, user_id)
    if user is None:
        abort(404)
    return jsonify({'user': user[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)