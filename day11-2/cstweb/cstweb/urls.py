"""
URL configuration for cstweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from . import views # import views.py bind urls to views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://localhost:8000/contact-us/ 
    path('contact-us/', views.contact_us, name='contact-us'),
    # http://localhost:8000/programs/
    path('programs/',views.processprograms,name='programs'),
    # http://localhost:8000/services/
    path('services/',views.processservices,name='services'),
    # http://localhost:8000/job-bank/
    path('job-bank/',views.processjob_bank,name='job-bank'),
    # http://localhost:8000/order/ point to apps order urls
     
    path('order/', include('order.urls')),


]
