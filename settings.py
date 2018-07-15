import os

host = 'localhost'
user = 'postgres_user'
password = 'postgres'
db = 'test_db'

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(
    host, db, user, password)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(os.getcwd(), 'cover')