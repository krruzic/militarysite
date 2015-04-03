from django.conf.urls import patterns, url

from simpleMilitary import views

urlpatterns = patterns('',
    url(r'register', views.register_page, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^searchResults', views.searchResults),
    url(r'^(?P<personnel_sin>\d+)/$', views.personnelDetail, name='personnelDetail'),
    url(r'^adminOperations', views.admin_operations, name='admin_operations'),
)