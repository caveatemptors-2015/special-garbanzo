from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class Analytics(View):
    def get(request, tricker_symbol = None):
        return render(request, 'quotes/analytics.html')


