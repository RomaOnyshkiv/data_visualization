from visualize.calculations import select_data


def get_available_years():
    my_db = "db.sqlite3"
    conn = select_data.create_connection(my_db)
    years = select_data.select_all_years(conn)
    return years


# print(get_available_years())
