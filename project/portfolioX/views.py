from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Portfolio, Security, Holding, Transaction
from . form_buy_new_security import PortfolioForm, HoldingForm, SecurityForm
from django.http import HttpResponse

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
			return redirect('portfolioX:add')
		else:
			return render(request, self.template_name, context)

class ListViewPortfolio(View):
	template_name = 'portfolioX/list_portfolio.html'

	def get(self, request):
		portfolio_list = Portfolio.objects.all()
		context = {'portfolio_list': portfolio_list}
		return render(request, self.template_name, context)

class SecurityAddView(View):
	template_name = 'portfolioX/add.html'

	def get(self, request):
		context = {'security':SecurityForm()}
		return render(request, self.template_name, context)

	def post(self, request):
		security_name = SecurityForm(request.POST)
		context = {'security':security_name}
		if security_name.is_valid():
			security = security_name.save()
			return redirect('portfolioX:holdings')
		else:
			return render(request, self.template_name, context)

class HoldingAddView(View):
	template_name = 'portfolioX/add_holding.html'

	def get(self, request, portfolio_id):
		portfolio = Portfolio.objects.get(pk=portfolio_id)
		context = {'portfolio_id':portfolio_id, 'form': HoldingForm(initial={portfolio:portfolio_id})}
		return render(request, self.template_name, context)

	def post(self, request, portfolio_id):
		holding_name = HoldingForm(request.POST)
		context = {'portfolio_id':portfolio_id, 'form':holding_name}
		if holding_name.is_valid():
			holding = holding_name.save()
			return redirect('portfolioX:holdings')
		else:
			return render(request, self.template_name, context)
	


class BuySellView(View):
	def get(self, request):
		return render(request, 'portfolioX/buysell.html')


class HoldingView(View):
	def get(self, request):
		return render(request, 'portfolioX/holdings.html')


















