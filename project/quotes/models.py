from django.db import models
import requests

# Create your models here.

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def get_quote(self,company):
		r = requests.get(self.quote_url+company)
		return r.json()
