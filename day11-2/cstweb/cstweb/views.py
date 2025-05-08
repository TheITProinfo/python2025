# thi is the views.py file

from django.shortcuts import render
from django.http import HttpResponse
def contact_us(request):
    return HttpResponse("This is the contact us page")
def processprograms(request):
    return HttpResponse("This is the process programs page")
def processservices(request):
   # return HttpResponse("This is the process services page")
   ## call render to render the template -hello.html
   # usually the context data is passed to the template as a dictionary, the data is passed as a key-value pair
   # the data is come from the database or any other source
   # for example, right now it is hardcode, but in real world, it will come from the database
   contex = {'name': 'Bob'} # this is the context data to be passed to the template
   return render(request, 'processservices.html', contex) # this is the way to retur

## this is proceess the job-ban function
def processjob_bank(request):
    return HttpResponse("This is the process job-bank page")