from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    usergroup = models.IntegerField()

    def __str__(self):
        return self.user

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
        return reverse('main_app:cart', args=[self.slug])

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_total(self):
        total = self.price * self.quantity
        return total


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    ordered_date = models.DateTimeField() 
    paid = models.BooleanField(default=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.user

    def get_total_order(self):
        return sum(item.get_total() for item in self.items.all())

