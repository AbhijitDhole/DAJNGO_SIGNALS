from django.shortcuts import render, HttpResponse

# Create your views here.
def home(self):
    a = 10/0
    return HttpResponse("ERROR!!")