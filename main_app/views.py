from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
 return render(request, 'about.html')

def checkout(request):
 return render(request, 'checkout.html')

def cart(request):
 return render(request, 'cart.html')
