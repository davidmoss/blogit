from django.conf import settings
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^auth/', include('auth.urls', namespace='auth')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^csp/', include('cspreports.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
