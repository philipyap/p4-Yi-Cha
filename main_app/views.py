from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Product, OrderItem, Order
from django.views.generic import DetailView
from django.conf import settings
from decimal import Decimal
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.

##### PRODUCTS #####
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter()
    return render(request, 'home.html', {'categories':categories,'products': products})

def product_details(request, product_id):
  # Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception
    product = Product.objects.get(id=product_id)
  # goto add_cart_form
  # cart_product_form = CartAddForm()
    return render(request, 'product.html', {'product': product})

##### CART #####


##### LOGIN VIEW
def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

#####  LOGOUT VIEW #####


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

##### Signup View #####

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def profile(request, username):
    user = User.objects.get(username=username)
    # cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username})

##### LOGIN_REQUIRED AND METHOD_DECORATOR ######

# Above the class CatDelete, add this line
# @method_decorator(login_required, name='dispatch')
# class CatDelete(DeleteView):

# Above the profile function, add this line
# @login_required
# def profile(request, username):



##### DEFAULTS #####

def about(request):
    return render(request, 'about.html')

def checkout(request):
    return render(request, 'checkout.html')

