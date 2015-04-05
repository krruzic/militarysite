from django.conf.urls import patterns, url

from simpleMilitary import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^searchResults', views.searchResults),
    url(r'^personnel/(?P<personnel_sin>\d+)/$', views.personnelDetail, name='personnelDetail'),
    url(r'^adminOperations', views.admin_operations, name='admin_operations'),
    url(r'^personnel/all', views.all_personnel, name='all_personnel'),
)