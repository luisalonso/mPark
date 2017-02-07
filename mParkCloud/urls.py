"""mParkCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'', include('mParkProfessional.urls')),

    url(r'^accounts/register/$', 'mParkProfessional.views.register', name='register'),
    url(r'^accounts/register/complete/$', 'mParkProfessional.views.registration_complete', name='registration_complete'),

    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'mParkProfessional.views.reset_confirm', name='password_reset_confirm'),
    url(r'^reset/$', 'mParkProfessional.views.reset', name='reset'),
    url(r'^reset/success/$', 'mParkProfessional.views.reset_success', name='reset_success'),
    url(r'^reset/complete/$', 'mParkProfessional.views.reset_complete', name='reset_complete'),
]
