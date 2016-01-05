from django.db import models

# Create your models here.

class Investor(models.Model):
	name = models.CharField(max_length=200)
	password = models.CharField(max_length=16)

class Security(models.Model):
	investor = models.ForeignKey(Investor)
	symbol = models.CharField(max_length = 50)
	url = models.URLField()    #gets all other info like symbol, price
	quantity = models.IntegerField()

class Transaction(models.Model):
	user = models.ForeignKey(Investor)
	symbol = models.ForeignKey(Security)
	quantity = models.IntegerField()
	txn_date = models.DateField()
	price = models.DecimalField(max_digits = 6, decimal_places = 2) 

