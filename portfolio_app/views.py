from django.shortcuts import render
from .models import portfolio

# Create your views here.
def home (request):
    portfolios=portfolio.objects.all()
    return render(request, 'index.html',{'portfolio':portfolios})