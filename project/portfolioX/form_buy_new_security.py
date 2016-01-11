from django import forms
from portfolioX.models import Security, Portfolio, Holding, Transaction

class SecurityForm(forms.ModelForm):
	class Meta:
		model = Security
		fields = ['ticker', 'company_name']

class PortfolioForm(forms.ModelForm):
	class Meta:
		model = Portfolio
		fields = ['portfolio_name', 'user']

class HoldingForm(forms.ModelForm):
	class Meta:
		model = Holding
		fields = ['portfolio', 'security', 'quantity', 'avg_price']
		widgets = {
			'portfolio': forms.HiddenInput()
		}
		

class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ['portfolio', 'symbol', 'quantity', 'txn_date', 'price']
	