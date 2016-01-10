from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HoldingView.as_view(), name='holdings'),
	url(r'^createportfolio', views.UserCreatePortfolio.as_view(), name='create_portfolio'),
	url(r'^list_portfolio', views.ListViewPortfolio.as_view(), name='list_portfolio'),
	url(r'^buysell/', views.BuySellView.as_view(), name='buysell'),
	url(r'^addremove/(?P<portfolio_id>[0-9])+', views.AddRemoveView.as_view(), name='addremove'),
	
]
