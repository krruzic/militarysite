from django.conf.urls import patterns, include, url
from django.contrib import admin
from simpleMilitary import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'militarysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^simpleMilitary/', include('simpleMilitary.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
