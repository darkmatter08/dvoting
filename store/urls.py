# Shawn Jain
# 1/16/2012
# This is the URL config for the store 'app'
from store import views #import first

from django.conf.urls import patterns, include, url
#from store.views import first

urlpatterns = patterns('',
	url(r'^$', views.firstfunc),
	url(r'^first/$', views.first)
)