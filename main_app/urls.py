from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='home'),
    path('about/', views.about, name='about'),
    path('product_details/<product_id>', views.product_details, name='product_details'),
    path('checkout/', views.order_create, name='checkout'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('create/', views.order_create, name='order_create'),
    path('user/<username>/create', views.ProfileCreate.as_view(), name='profile_create'),
    path('user/<username>/update', views.ProfileUpdate.as_view(), name='profile_update'),
    path('user/<username>/<int:pk>/delete', views.OrderDelete.as_view(), name='order_delete')

]