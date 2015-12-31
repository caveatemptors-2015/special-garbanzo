from django.shortcuts import render

# Create your views here.
def buysell(request):
	return render(request, 'portfolioX/buysell.html')

def addremove(request):
	return render(request, 'portfolioX/addremove.html')

def holdings(request):
	return render(request, 'portfolioX/holdings.html')
