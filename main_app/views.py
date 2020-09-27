from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, OrderItem, Order
from django.views.generic import DetailView
from django.conf import settings
from decimal import Decimal

# Create your views here.

##### PRODUCTS #####
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter()
    return render(request, 'home.html', {'categories':categories,'products': products})

def product_details(request, product_id):
  # Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception
  product = Product.objects.get(Product, id=product_id)
  # goto add_cart_form
  # cart_product_form = CartAddForm()
  return render(request, 'cart.html', {'product': product} )

##### CART #####
class Cart(object):
  # __init__ setting user's requests to various parts of a web site
  def __init__(self,request):
    self.session = request.session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
      cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart

  # define add quantity
  def add(self, product, quantity=1, update_quantity=False):
    product_id = str(product.id)
    if product_id not in self.cart:
      self.cart[product_id] = {'quantity':0, 'price':str(product_id.price)}
    if update_quantity:
      self.cart[product_id]['quantity'] = quantity
    else:
      self.cart[product_id]['quantity'] += quantity
    self.save()

  def save(self):
    self.session.modified = True

  # define remove item
  def remove(self, product):
    product_id = str(product.id)
    if product_id in self.cart:
      del self.cart[product_id]
      self.save()

  #  reset the starting point of the iteration
  def __iter__(self):
    product_ids = self.cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    # call twice in copy()
    cart = self.cart.copy()
    for product in products:
      cart[str(product.id)]['product'] = product
    for item in cart.values():
      item['price']=Decimal(item['price'])
      item['total_price']=item['price'] * item['quantity']
      yield item
    
  def __len__(self):
    return sum(item['quantity'] for item in self.cart.values())

  def get_total_price(self):
    return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

  def clear(self):
    del self.session[settings.CART_SESSION_ID]
    self.save()

##### DEFAULTS #####

def about(request):
 return render(request, 'about.html')

def checkout(request):
 return render(request, 'checkout.html')

