from django.conf.urls import patterns, url

from simpleMilitary import views

urlpatterns = patterns('',
    url(r'^$', views.searchResults, name='searchResults'),    
)