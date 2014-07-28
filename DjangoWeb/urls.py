from django.conf.urls import patterns, include, url

from django.contrib import admin
from pythonWeb.views import *

admin.autodiscover()

urlpatterns = patterns('pythonWeb.views',
    # Examples:
    # url(r'^$', 'DjangoWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', 'current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^show_list/$', 'show_list'),
    url(r'^insert_user/$', 'insert_user'),
    url(r'^show_user/$', 'show_user'),
    url(r'^show_user_name/(\w+)/$', 'show_user_name'),
    url(r'^echo_once/$', 'echo_once'),

)
