from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^01/$', 'a_01.views.home'),
    url(r'^02/$', 'a_02.views.home'),
    url(r'^02/xq/$', 'a_02.views.xquery'),
    url(r'^03/$', 'a_03.views.home')
    # Examples:
    # url(r'^$', 'WE_assignment.views.home', name='home'),
    # url(r'^WE_assignment/', include('WE_assignment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
