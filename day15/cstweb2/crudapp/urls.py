
from django.urls import path

from . import views


urlpatterns = [ 
    path('', views.showView, name='home_url'), 
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
    path('detail/<int:f_oid>/', views.detailView, name='detail_url'),
]