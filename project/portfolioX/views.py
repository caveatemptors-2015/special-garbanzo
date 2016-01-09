from django.shortcuts import render
from django.views.generic import View


class UserCreatePortfolio(View):
	template_name = 'portfolioX/create_portfolio.html'
	
	def post(self, request, user_id):
		pass



class BuySellView(View):
	def get(self, request):
		return render(request, 'portfolioX/buysell.html')

class AddRemoveView(View):
	def get(self, request):
		return render(request, 'portfolioX/addremove.html')

class HoldingView(View):
	def get(self, request):
		return render(request, 'portfolioX/holdings.html')
