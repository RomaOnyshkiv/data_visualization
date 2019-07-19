import requests
import pygal
from pygal.style import LightColorizedStyle as DCS, LightenStyle as LS


def generate_rating_file(lang):
    url = 'https://api.github.com/search/repositories?q=language:' + str(lang) + '&sort=starts'
    r = requests.get(url)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    names, stars = [], []

    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])

    my_style = LS('#333366', base_style=DCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred ' + str(lang) + ' Projects on GitHub'
    chart.x_labels = names
    chart.add(' ', stars)
    return chart.render_to_file('visualize/static/visualize/repos.svg')
