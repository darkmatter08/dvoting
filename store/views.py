# Shawn Jain 
# 1/16/2013
# Store project
# views.py

# This file defines the logic to display the page. Methods are 
# invoked automatically when a url is matched in urls.py

#imports
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from store.models import *
from django.shortcuts import render

# Functions to test out the proper working of the 'store' app
def firstfunc(request):
	return HttpResponse("First view in an app, man!\nThis is firstfunc")

def first(request):
	return HttpResponse("First view in an app, man!\nThis is first")

# The proper functions for this store app
# See the homepage with a greeting, and a button to view orders and a button to place orders
def home(request):
	t = get_template("home.html")
	html = t.render(Context({"my_name": "ShawnJainInFunc"}))
	return HttpResponse(html)

# This view creates a form that has space to enter 2 different products for a user to buy
def place(request):
	return render(request, 'placeorder.html', {'form': OrderForm()})

# method to process order request
def placeapi(request):
	return HttpResponse("placeholder")

# This view lists all the orders
def viewall(request):
	t = get_template("orders.html")
	html = t.render(Context({"my_name": "ShawnJainInFunc"}))
	return HttpResponse(html)

# This funciton is testing out the ability to grab info about
# the user from the request, including but not limited to the user agent string
def showinfo(request):
	path = request.path
	host = request.get_host()
	fullpath = request.get_full_path()
	isSecure = request.is_secure()
	return HttpResponse("path="+path+" | host="+host+" | fullpath="+fullpath+" | isSecure="+str(isSecure))