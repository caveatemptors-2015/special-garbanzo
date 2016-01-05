from django import forms
from portfolioX.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction 
        fields = ['symbol', 'quantity','price'] 