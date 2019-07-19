from visualize.calculations import select_data

my_db = "db.sqlite3"


def get_available_years():
    conn = select_data.create_connection(my_db)
    years = select_data.select_all_years(conn)
    return years


def get_available_languages():
    conn = select_data.create_connection(my_db)
    languages = select_data.select_all_languages(conn)
    return languages
