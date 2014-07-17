from django.conf.urls import patterns, include, url

from django.contrib import admin
from pythonWeb.views import current_datetime
from pythonWeb.views import hours_ahead
from pythonWeb.views import show_list
from pythonWeb.views import insert_user

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^show_list/$', show_list),
    url(r'^insert_user/$', insert_user),
)
