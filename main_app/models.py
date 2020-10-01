from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phone_field import PhoneField

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    usergroup = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField()
    price = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cart_detail')



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    ordered_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_order(self):
        return sum(item.get_total() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    # amount = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_total(self):
        total = self.price * self.quantity
        return total