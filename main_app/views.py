from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Product, OrderItem, Order, UserProfile
from django.views.generic import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .cart import Cart, CartAddProductForm, OrderCreateForm
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.

##### PRODUCTS #####
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter()
    # parse-in cart form for quantity/update
    cart_product_form = CartAddProductForm()
    # grab class Cart info 
    cart = Cart(request)
    for item in cart:
      item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'home.html', {'categories':categories,'products': products, 'cart_product_form': cart_product_form, 'cart': cart})

def product_details(request, product_id):
  # Calls get() on a given model manager
    product = Product.objects.get(id=product_id)
  # for icon cart length
    cart = Cart(request)
    for item in cart:
      item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
  
    return render(request, 'product.html', {'product': product, 'cart': cart})

##### CART #####
def cart_detail(request):
  cart = Cart(request)
  for item in cart:
      item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
  return render(request, 'cart.html', {'cart': cart})

def cart_add(request, product_id):
  cart = Cart(request)
  product = get_object_or_404(Product, id=product_id)
  # POST update quantity in cart and 
  # set the form is valid then save the data by using form.cleaned_data
  form = CartAddProductForm(request.POST)
  if form.is_valid():
      cd = form.cleaned_data
      cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
  return redirect('cart_detail')

# class QtyUpdate(UpdateView):
#   model: Product

#   def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
#         self.object = form.save(commit=False) # Don't immediately post to the db until we say so
#         self.object.save()
#         return HttpResponseRedirect('/cart_detail')
  
  

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

##### ORDER #####

def order_create(request):
  cart = Cart(request)
  user = User.objects.get(username=request.user.username)
  # if post, then goto form
  if request.method == 'POST':
    # form = OrderCreateForm(request.POST)
    order = Order.objects.create(user=user, first_name=request.POST['first_name'], last_name=request.POST['last_name'], shipping_address=request.POST['shipping_address'], email=request.POST['email'])
    #if form valid, create the OrderItem
    # if form.is_valid():
    #   order = form.save()
    for item in cart:
      OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
      # clear cart info once created OrderItem
    cart.clear()
      # email to customer once order proceeds
      # 
    return render(request, 'checkout.html', {'order': order})
    
  else:
    form = OrderCreateForm()
  return render(request, 'order.html', {'cart': cart, 'form': form})

@method_decorator(login_required, name='dispatch')
class ProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'
    
    def get_success_url(self):
        return '/user/'+self.request.user.username+'/'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        print('!!!! SELF.OBJECT:', self.object)
        self.object.user = self.request.user
        self.oblect.save()
        return '/user/'+self.request.user.username+'/'+str(self.object.pk)


class ProfileUpdate(UpdateView):
    
    model = UserProfile
    fields = ['first_name', 'last_name', 'phone', 'email']

    def form_valid(self, form):
        print(self.request)
       # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # don't post to the db until we say so

        self.object.save()
        return render('/user/'+self.request.user.username+'/')

class OrderDelete(DeleteView):
    model = Order

    def get_success_url(self):
        return '/user/'+self.request.user.username+'/'

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
    print(user.id)
    order = Order.objects.filter(user=user)
    user_profile = UserProfile.objects.filter(user=user)
    # for icon cart length
    cart = Cart(request)
    for item in cart:
      item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    
    return render(request, 'profile.html', {'user': user, 'username': username, 'order': order, 'cart': cart, 'user_profile': user_profile})


##### DEFAULTS #####

def about(request):
  # for icon cart length 
    cart = Cart(request)
    for item in cart:
      item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'about.html', {'cart':cart})

