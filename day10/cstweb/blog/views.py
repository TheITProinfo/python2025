from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    data=dict()
    # return render(request, 'home.html',data)
    return HttpResponse("Hello, Blog!") # response to the client
def about(request):
    return HttpResponse("About Us page!!!") # response to the client

## define contact view function here
def contact(request):
    return HttpResponse("Contact Us page!!!") # response to the client