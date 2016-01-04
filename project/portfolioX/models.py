from django.db import models
import requests

# Create your models here.

class Investor(models.Model):
	name = models.CharField(max_length=200)
	password = models.CharField(max_length=16)

class Security(models.Model):
	symbol = models.CharField(max_length = 50)
	url = models.URLField()
	
class Porfolios(models.Model):
	investor = models.ForeignKey(Investor)
	security = models.ForeignKey(Security)
	quantity = models.IntegerField(100)
	txn_date = models.DateField()
	porfolio_name = models.CharField(max_length=200)

	

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def get_quote(self,company):
		r = requests.get(self.quote_url+company)
		return r.json()
