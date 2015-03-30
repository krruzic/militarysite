from django.conf.urls import patterns, url

from simpleMilitary import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^searchResults', views.searchResults),        
=======
    url(r'^(?P<personnel_sin>\d+)/$', views.personnelDetail, name='personnelDetail'),
>>>>>>> 7c959681d7f74ed19f955f0e41a046a6e29f4f46
)