from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from simpleMilitary import views
from django.views.generic import RedirectView
admin.site.login = views.login_user
admin.site.logout = views.logout_user

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='simpleMilitary/')),
    url(r'^simpleMilitary/', include('simpleMilitary.urls', namespace="simpleMilitary")),
    url(r'^accounts/login/$', views.login_user),
    url(r'^accounts/logout/$', views.logout_user),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/register', views.register_page),
)
