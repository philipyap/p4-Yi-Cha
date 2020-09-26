from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product

# Create your views here.

##### PRODUCTS #####
def product_list(request):
  categories = Category.objects.all()
  products = Product.objects.filter(name)
  return render(request, 'home.html', {'categories': categories, 'products': products})

##### DEFAULTS #####

def about(request):
 return render(request, 'about.html')

def checkout(request):
 return render(request, 'checkout.html')

def cart(request):
 return render(request, 'cart.html')
