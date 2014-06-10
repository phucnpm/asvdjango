from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asvdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dojango/', include('apps.dojango.urls')),
    url(r'^demo/', include('demo.urls')),

    # url(r'^$', 'apps.dojango.views.test'),
    url(r'^$', 'demo.views.mydojo'),
)
