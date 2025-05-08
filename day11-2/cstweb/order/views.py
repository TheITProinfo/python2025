from django.shortcuts import render, HttpResponse

# Create your views here.
## this is the home page for processing orders
def processhome(request):
    return HttpResponse("Hello, world. You're at the process order home.")
def total(request):
    return HttpResponse("Hello, world. You're at the total page.")  
def process(request):
    return HttpResponse("Hello, world. You're at the process page.")
def payment(request):
    return HttpResponse("Hello, world. You're at the payment page.")
def checkout(request):
    return HttpResponse("Hello, world. You're at the checkout page.")