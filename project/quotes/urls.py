from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<ticker_symbol>.*)', views.analytics, name='analytics'),
]
