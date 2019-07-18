from django.shortcuts import render
from .calculations.create_file import generate_result_file
from .calculations.years import get_available_years


def index(request):
    """ View for home page"""
    all_years = []
    years = get_available_years()
    for y in years:
        all_years.append(str(y[0]))
    context = {'years': all_years}
    return render(request, 'visualize/index.html', context)


def results(request, year):
    """ View for results """
    generate_result_file(int(year))
    return render(request, 'visualize/results.html')


def abut(request):
    """ View for app description"""
    return render(request, 'visualize/about.html')

