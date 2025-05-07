from django.urls import path
from . import views
app_name = 'mobile'
urlpatterns = [
    path('', views.home, name='home'), # http://127.0.0.0/mobile
]
