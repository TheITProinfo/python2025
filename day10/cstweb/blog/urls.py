# this is app-blog urls.py
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'), # https://127.0.0.1:8000/blog/
    path('about/', views.about, name='about'), # https://127.0.0.1:8000/blog/about/
    path('contact/', views.contact, name='contact'), # https://127.0.0.1:8000/blog/contact/

]