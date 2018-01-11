"""
Definition of urls for daZibao.
"""

from django.conf.urls import include, url
from django.contrib.staticfiles.urls import urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', daZibao.views.home, name='home'),
    # url(r'^daZibao/', include('daZibao.daZibao.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
