from django import forms
from portfolioX.models import Security, Portfolio, Holding, Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction 
        fields = ['symbol', 'quantity','price']

class Securiy(forms.ModelForm):
	class Meta:
		model = Security
		fields = ['ticker', 'company_name']

class Portfolio(forms.ModelForm):
	class Meta:
		model = Portfolio
		fields = ['portfolio_name', 'user']

class Holding(forms.ModelForm):
	class Meta:
		model = Holding
		fields = ['portfolio', 'security', 'quantity', 'avg_price']

class Transaction(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ['portfolio', 'symbol', 'quantity', 'txn_date', 'price']
	