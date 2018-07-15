import psycopg2
import settings


def db_executor(sql_query=None, stipulation=None):
    conn = psycopg2.connect(settings.conn_string)
    cur = conn.cursor()
    if stipulation:
        cur.execute(sql_query, (stipulation,))
        res = cur.fetchone()
    else:
        cur.execute(sql_query)
        res = cur.fetchall()
    return res
