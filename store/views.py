# Shawn Jain 
# 1/16/2013
# Store project
# views.py

# This file defines the logic to display the page. Methods are 
# invoked automatically when a url is matched in urls.py

#imports
from django.http import HttpResponse
from django.template import Template, Context

# Functions to test out the proper working of the 'store' app
def firstfunc(request):
	return HttpResponse("First view in an app, man!\nThis is firstfunc")

def first(request):
	return HttpResponse("First view in an app, man!\nThis is first")

# The proper functions for this store app
# See the homepage with a greeting, and a button to view orders and a button to place orders
def home(request):
	return HttpResponse("Blank")

# This view creates a form that has space to enter 2 different products for a user to buy
def place(request):
	return HttpResponse("Blank")

# This view lists all the orders
def viewall(request):
	return HttpResponse("Blank")