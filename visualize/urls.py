""" URLs for visualization app"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'results/(?P<year>\d+)/$', views.results, name='results'),
    url(r'^about/$', views.about, name='about'),
    url(r'^remote/(?P<lang>\w+)/$', views.remote, name='remote'),

]
