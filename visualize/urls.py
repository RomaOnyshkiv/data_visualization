""" URLs for visualization app"""
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'results/(?P<year>\d+)/$$', views.results, name='results'),
    url(r'^about/$', views.abut, name='about'),

]

# urlpatterns += staticfiles_urlpatterns()
