from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from simpleMilitary import views

urlpatterns = patterns('',
    url(r'^simpleMilitary/', include('simpleMilitary.urls', namespace="simpleMilitary")),
    url(r'^accounts/login/$', views.login_user),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/register', views.register_page),
)
