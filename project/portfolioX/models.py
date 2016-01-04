from django.db import models

# Create your models here.

class Investor(models.Model):
	name = models.CharField(max_length=200)
	password = models.CharField(max_length=16)

class Security(models.Model):
	symbol = models.CharField(max_length = 50)
	url = models.URLField()
	quantity = models.IntegerField(100)
	investor = models.ForeignKey(Investor)

class Transaction(models.Model):
	quantity = models.IntegerField(1000)
	symbol = models.ForeignKey(Security)
	txn_date = models.DateField() 

