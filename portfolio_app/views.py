from django.shortcuts import render
from .models import portfolio,review

# Create your views here.
def home (request):
    portfolios=portfolio.objects.all()
    reviews=review.objects.all()
    return render(request, 'index.html',{'portfolio':portfolios,'review':reviews})