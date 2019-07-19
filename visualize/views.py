from django.shortcuts import render
from .calculations.create_file import generate_result_file
from .calculations.years import get_available_years, get_available_languages
from .requests.externalData import generate_rating_file


def index(request):
    """ View for home page"""
    all_langs = __generate_context(get_available_languages())
    all_years = __generate_context(get_available_years())
    all_years.reverse()
    all_langs.sort()
    context = {'years': all_years, 'langs': all_langs}
    return render(request, 'visualize/index.html', context)


def results(request, year):
    """ View for results """
    all_years = __generate_context(get_available_years())
    all_years.reverse()
    context = {'years': all_years}
    generate_result_file(year=int(year))
    return render(request, 'visualize/results.html', context)


def about(request):
    """ View for app description"""
    return render(request, 'visualize/about.html')


def remote(request, lang):
    """ View for results from git """
    all_langs = __generate_context(get_available_languages())
    all_langs.sort()
    context = {'langs': all_langs}
    generate_rating_file(lang=str(lang))
    return render(request, 'visualize/remote.html', context)


def __generate_context(my_list):
    tmp_list = []
    for item in my_list:
        tmp_list.append(str(item[0]))
    return tmp_list
