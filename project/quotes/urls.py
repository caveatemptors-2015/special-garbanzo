from django.conf.urls import url
from . import views
from quotes.views import Analytics

urlpatterns = [
	url(r'^(?P<ticker_symbol>.*)', Analytics.as_view(), name='analytics'),
]
