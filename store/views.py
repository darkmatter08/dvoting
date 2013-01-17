# Shawn Jain 
# 1/17/2013
# Store project
# views.py

# This file defines the logic to display the page. Methods are 
# invoked automatically when a url is matched in urls.py

#imports
from django.http import HttpResponse

def firstfunc(request):
	return HttpResponse("First view in an app, man!\nThis is firstfunc")

def first(request):
	return HttpResponse("First view in an app, man!\nThis is first")
