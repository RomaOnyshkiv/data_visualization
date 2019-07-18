from visualize.calculations import select_data
from pygal_maps_world import maps
from pygal.style import RotateStyle, LightColorizedStyle, DarkColorizedStyle
from visualize.calculations.country_codes import get_country_code
import os

cc_populations = {}
file_path = 'visualize/static/visualize/map.svg'


def delete_file():
    os.remove(file_path)


def generate_result_file(year):
    my_db = "db.sqlite3"
    conn = select_data.create_connection(my_db)
    with conn:
        dataset = select_data.select_by_year(conn, str(year))
        for data in dataset:
            country_name = data[1]
            population = data[3]
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population
            else:
                cc_populations["na"] = 0

    for data in dataset:
        country_name = data[1]
        population = data[3]
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            cc_populations["na"] = 0

    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

    for cc, my_pop in cc_populations.items():
        pop = int(float(my_pop))
        if pop < 10000000:
            cc_pops_1[cc] = pop
        elif pop < 1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop

    wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
    wm = maps.World(style=wm_style)
    wm.title = 'World populations in ' + str(year) + ', by country'
    wm.add('0 - 10m', cc_pops_1)
    wm.add('10m - 1bn', cc_pops_2)
    wm.add('>1bn', cc_pops_3)
    return wm.render_to_file(file_path)
