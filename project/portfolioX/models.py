from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
# 	name = models.CharField(max_length=200)
# 	password = models.CharField(max_length=16)
class Security(models.Model):
	ticker = models.CharField(max_length = 100)
	company_name = models.CharField(max_length = 255)

class Portfolio(models.Model):
	portfolio_name = models.CharField(max_length = 255)
	user = models.ForeignKey(User)
	

class Holding(models.Model):
	portfolio = models.ForeignKey(Portfolio)
	security = models.ForeignKey(Security)
	quantity = models.IntegerField()
	avg_price = models.DecimalField(max_digits = 6, decimal_places = 2) #calculated and updated

class Transaction(models.Model):
	portfolio = models.ForeignKey(Portfolio)
	symbol = models.ForeignKey('Security')
	quantity = models.IntegerField()
	txn_date = models.DateTimeField(auto_now_add=False)
	price = models.DecimalField(max_digits = 6, decimal_places = 2) 

