from django.conf.urls import url
from . import views

print(dir(views))

urlpatterns = [
	url(r'^$', views.HoldingView.as_view(), name='holdings'),
	url(r'^createportfolio$', views.UserCreatePortfolio.as_view(), name='create_portfolio'),
	url(r'^list_portfolio$', views.ListViewPortfolio.as_view(), name='list_portfolio'),
	url(r'^buysell/$', views.BuySellView.as_view(), name='buysell'),
	url(r'^add/$', views.SecurityAddView.as_view(), name='add'),
	url(r'^add_holding/(?P<portfolio_id>[0-9]+)/$', views.HoldingAddView.as_view(), name='add_holding'),
	url(r'^all_holding/(?P<portfolio_id>[0-9]+)/$', views.HoldingAllView.as_view(), name='all_holding'),
	url(r'^all_holding/(?P<portfolio_id>[0-9]+)/update_holding/(?P<holding_id>[0-9]+)/$', views.HoldingUpdateView.as_view(), name='update_holding'),
]
