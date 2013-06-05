
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^$', 'taxation.views.index', name='index'),
    url(r'^description/add/$', 'taxation.views.description_add', name='description_add'),
    url(r'^description/(?P<did>\d+)/$', 'taxation.views.description_view', name='description_view'),
    url(r'^description/(?P<did>\d+)/edit/$', 'taxation.views.description_edit', name='description_edit'),
    url(r'^description/(?P<did>\d+)/card/add/$', 'taxation.views.card_add', name='card_add'),
    url(r'^description/(?P<did>\d+)/card/(?P<cid>\d+)/$', 'taxation.views.card_view', name='card_view'),
    url(r'^description/(?P<did>\d+)/card/(?P<cid>\d+)/edit/$', 'taxation.views.card_edit', name='card_edit'),
    # url(r'^$', 'academy.views.home', name='home'),
    # url(r'^academy/', include('academy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()