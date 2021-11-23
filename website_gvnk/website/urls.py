from django.urls import path
from django.urls import path
from. import views 

urlpatterns = [
    path('', views.indexView, name="home"),
    path('products/', views.productsView, name="products"),
    path('contact/', views.contactView, name="contact"),
    path('cart/', views.cartView, name="cart"),
    





]