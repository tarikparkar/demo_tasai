from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is my first response")

# Create your views here.
