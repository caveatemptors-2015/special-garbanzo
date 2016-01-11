from django.db import models
from django.contrib.auth.models import User


class Security(models.Model):
	ticker = models.CharField(max_length = 100)
	company_name = models.CharField(max_length = 255)

	def __str__(self):
		return self.company_name

class Portfolio(models.Model):
	portfolio_name = models.CharField(max_length = 255)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.portfolio_name
	

class Holding(models.Model):
	portfolio = models.ForeignKey(Portfolio)
	security = models.ForeignKey(Security)
	quantity = models.IntegerField()
	avg_price = models.DecimalField(max_digits = 6, decimal_places = 2)


class Transaction(models.Model):
	portfolio = models.ForeignKey(Portfolio)
	symbol = models.ForeignKey('Security')
	quantity = models.IntegerField()
	txn_date = models.DateTimeField(auto_now_add=False)
	price = models.DecimalField(max_digits = 6, decimal_places = 2) 

