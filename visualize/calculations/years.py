from visualize.calculations.select_data import select_all_years, create_connection, select_all_languages


def get_available_years():
    return select_all_years(create_connection())


def get_available_languages():
    return select_all_languages(create_connection())
