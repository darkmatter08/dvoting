from django.conf.urls import patterns, include, url
from voting import views
from django.views.generic import simple
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from store import urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voting.views.home', name='home'),
    # url(r'^voting/', include('voting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #landing page, works with views.home
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
 	#Home view!
    url(r'^home/$', views.home),
    #Store app view
    url(r'^store/', include('store.urls')),
    #url(r'^store/', store.views.first),
)

urlpatterns += staticfiles_urlpatterns()