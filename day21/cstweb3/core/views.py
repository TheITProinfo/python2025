from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def contact(request):
    return render(request, 'core/contact.html') 
def login(request):
    return render(request, 'core/login.html') 
def signup(request):
    return render(request, 'core/signup.html')