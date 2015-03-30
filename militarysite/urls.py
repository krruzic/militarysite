from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from simpleMilitary import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'militarysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^simpleMilitary/', include('simpleMilitary.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/simpleMilitary/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
)
