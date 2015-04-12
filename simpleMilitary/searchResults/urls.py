from django.conf.urls import patterns, url

from simpleMilitary import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^$', views.searchResults, name='searchResults'),      
)