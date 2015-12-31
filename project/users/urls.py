from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.welcome, name='welcome'),
	url(r'^login$', views.login_, name='login'),
	url(r'^register$', views.register, name='register'),
]
