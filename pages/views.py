from django.http import HttpResponse #(lets u use python in django)
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): #python lets u pass any arguements and key arguements
    return HttpResponse ("<h1>Hello world</h1>") #string of html code
