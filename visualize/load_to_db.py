import json
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def write_data(conn, record):
    sql = '''INSERT INTO visualize_country(country_name,country_code,year,value)
              VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, record)
    return cur.lastrowid


def main():
    filename = 'population_data_upd.json'
    my_db = '/Users/roma/PycharmProjects/data_visualization/db.sqlite3'

    with open(filename) as f:
        population_data = json.load(f)

    conn = create_connection(my_db)
    with conn:
        for pop in population_data:
            country_name = pop["Country Name"]
            country_code = pop["Country Code"]
            year = pop["Year"]
            value = pop["Value"]
            my_record = [country_name, country_code, year, value]
            print(my_record)
            write_data(conn, my_record)


if __name__ == '__main__':
    main()
