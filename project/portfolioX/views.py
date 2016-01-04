from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class BuySellView(View):
	def get(self, request):
		return render(request, 'portfolioX/buysell.html')

class AddRemoveView(View):
	def get(self, request):
		return render(request, 'portfolioX/addremove.html')

class HoldingView(View):
	def get(self, request):
		return render(request, 'portfolioX/holdings.html')
