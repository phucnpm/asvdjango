from django import VERSION as django_version
if django_version >= (1, 5, 0):
    from django.conf.urls import patterns, url
else:
    from django.conf.urls.defaults import *

from demo import views

urlpatterns = patterns('demo',
    url(r'^mydojo/$', 'views.mydojo', name='mydojo'),
)


