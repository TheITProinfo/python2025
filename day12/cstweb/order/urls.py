

from django.urls import path

from . import views


urlpatterns = [
    # list of orders
    # http://localhost:8000/order/
    path('', views.order_list, name='order_list'),
    # http://localhost:8000/order/create/
    path('create/', views.create_order, name='create_order'),
    # http://localhost:8000/order/update/1/
    
    path('update/<int:order_id>', views.update_order, name='update_order'),
    # http://localhost:8000/order/delete/1/
    path('delete/<int:order_id>', views.delete_order, name='delete_order'),
]