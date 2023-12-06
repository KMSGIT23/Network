import pymysql
import pymysql.cursors

def insert_sql(scan):
    conn = pymysql.connect(host="localhost", user='root', password='1234', db='umbrella')
    try:
        with conn.cursor() as cursor:
            cursor.execute('insert into loan values(%s, %s, now(), date_add(now(), INTERVAL 7 DAY))'%(scan, ))
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def delete_sql(scan):
    conn = pymysql.connect(host="localhost", user='root', password='1234', db='umbrella')
    try:
        with conn.cursor() as cursor:
            cursor.execute('DELETE from loan where sid = %s' %scan)
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def select_sql():
    results = None
    conn = pymysql.connect(host="localhost", user='root', password='1234', db='umbrella')
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT sid, uid, borrow_date, return_date FROM loan')
            results = cursor.fetchall()
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    return results
