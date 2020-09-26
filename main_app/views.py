from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

# Create your views here.

##### PRODUCTS #####
def product_list(request):
  categories = Category.objects.all()
  products = Product.objects.filter(name)
  return render(request, 'home.html', {'categories': categories, 'products': products})

def product_details(request, id):
  # Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception
  product = get_object_or_404(Product, id=id)
  # goto add_cart_form
  # cart_product_form = CartAddForm()
  return render(request, 'cart.html', {'product': product} )


##### DEFAULTS #####

def about(request):
 return render(request, 'about.html')

def checkout(request):
 return render(request, 'checkout.html')

