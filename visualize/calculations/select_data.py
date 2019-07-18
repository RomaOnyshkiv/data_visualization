import sqlite3
from sqlite3 import Error


def create_connection(my_db):
    print(my_db)
    try:
        conn = sqlite3.connect(my_db)
        print('connected')
        return conn
    except Error as e:
        print(e)
    return None


def select_by_year(conn, year):
    cur = conn.cursor()
    print(year)
    cur.execute("SELECT * FROM visualize_country WHERE year=?", (year,))
    rows = cur.fetchall()
    return rows


def select_all_years(conn):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT year FROM visualize_country")
    all_years = list(cur.fetchall())
    return all_years


