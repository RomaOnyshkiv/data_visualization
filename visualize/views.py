from django.shortcuts import render
from .calculations.create_file import generate_result_file
from .calculations.years import get_available_years, get_available_languages
from .requests.externalData import generate_rating_file


def index(request):
    """ View for home page"""
    all_langs = []
    all_years = []

    for l in get_available_languages():
        all_langs.append(str(l[0]))

    for y in get_available_years():
        all_years.append(str(y[0]))

    all_years.reverse()
    all_langs.sort()
    context = {'years': all_years, 'langs': all_langs}

    return render(request, 'visualize/index.html', context)


def results(request, year):
    """ View for results """
    generate_result_file(year=int(year))
    return render(request, 'visualize/results.html')


def about(request):
    """ View for app description"""
    return render(request, 'visualize/about.html')


def remote(request, lang):
    """ View for results from git """
    generate_rating_file(lang=str(lang))
    return render(request, 'visualize/remote.html')
