from django.shortcuts import render

# Create your views here.

def analytics(request, ticker_symbol=None):
	return render(request, 'quotes/analytics.html')
