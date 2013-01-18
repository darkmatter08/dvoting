# Shawn Jain
# 1/16/2012
# This is the URL config for the store 'app'
from store import views

from django.conf.urls import patterns, include, url
#from store.views import first

urlpatterns = patterns('',
	# Test URLs to see if they are processed by django properly
	url(r'^firstfunc/$', views.firstfunc),
	url(r'^first/$', views.first),

	# proper URL structure
	#homepage
	url(r'^$', views.home),
	# Place an order
	url(r'^place/$', views.place),
	# view all orders
	url(r'^view/$', views.viewall),
)