# Shawn Jain
# 1/16/2013
# Data Models within the store app

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=30)
	addr = models.CharField(max_length=50)

	#Describes the object when it is called from the DB
	def __unicode__(self):
		return self.name

	#Default ordering attribute:
	class Meta:
			ordering = ['name']

class Order(models.Model):
	oid = models.IntegerField()
	# Many to one relationship with customer
	mycust = models.ForeignKey(Customer)

	def __unicode__(self):
		return self.oid

class Product(models.Model):
	pid = models.IntegerField()
	#Many to one relationship with Orders
	myorder = models.ForeignKey(Order)
	description = models.CharField(max_length=50)

	def __unicode__(self):
		return self.description

# Class to make an order form
class OrderForm(ModelForm):
	class Meta:
		model = Order

# Class to make a customer form for new customers
class CustomerForm(ModelForm):
	class Meta:
		model = Customer