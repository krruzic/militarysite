from django.conf.urls import patterns, include, url
from django.contrib import admin
from simpleMilitary import views

urlpatterns = patterns('',
    url(r'^simpleMilitary/', include('simpleMilitary.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
