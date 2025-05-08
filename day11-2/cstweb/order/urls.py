
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/order/home
#    path('home/', views.processhome,name='home'),
     path('', views.processhome,name='home'),
     path('total/', views.total,name='total'),
     path('process/', views.process,name='process'),
     path('checkout/', views.checkout,name='checkout'),
]