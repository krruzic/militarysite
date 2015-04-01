from django.conf.urls import patterns, url

from simpleMilitary import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^searchResults', views.searchResults),        
    url(r'^(?P<personnel_sin>\d+)/$', views.personnelDetail, name='personnelDetail'),
)