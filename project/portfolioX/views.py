from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Portfolio, Security, Holding, Transaction
from . form_buy_new_security import PortfolioForm


class UserCreatePortfolio(View):
	template_name = 'portfolioX/create_portfolio.html'
	
	def get(self, request):
		context = {'form': PortfolioForm(initial={'user':request.user.id})}
		return render(request, self.template_name, context)

	def post(self, request):
		portfolio_name = PortfolioForm(request.POST)
		context = {'form': portfolio_name}
		if portfolio_name.is_valid():
			portfolio = portfolio_name.save()
			return redirect('portfolioX:addremove')
		else:
			return render(request, self.template_name, context)

class ListViewPortfolio(View):
	template_name = 'portfolioX/list_portfolio.html'

	def get(self, request):
		portfolio_list = Portfolio.objects.all()
		context = {'portfolio_list': portfolio_list}
		return render(request, self.template_name, context)



class BuySellView(View):
	def get(self, request):
		return render(request, 'portfolioX/buysell.html')

class AddRemoveView(View):
	def get(self, request):
		return render(request, 'portfolioX/addremove.html')

class HoldingView(View):
	def get(self, request):
		return render(request, 'portfolioX/holdings.html')
