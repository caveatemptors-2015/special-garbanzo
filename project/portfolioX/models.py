from django.db import models
from users.models import User

# Create your models here.

# class User(models.Model):
# 	name = models.CharField(max_length=200)
# 	password = models.CharField(max_length=16)

class Security(models.Model):
	user = models.ForeignKey(User)
	symbol = models.CharField(max_length = 50)
	quantity = models.IntegerField()
	avg_price = models.DecimalField(max_digits = 6, decimal_places = 2) #calculated and updated

class Transaction(models.Model):
	user = models.ForeignKey(User)
	symbol = models.ForeignKey(Security)
	quantity = models.IntegerField()
	txn_date = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits = 6, decimal_places = 2) 

