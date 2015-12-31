from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^buysell/', views.buysell, name='buysell'),
	url(r'^addremove/', views.addremove, name='addremove'),
	url(r'^', views.holdings, name='holdings'),
]
