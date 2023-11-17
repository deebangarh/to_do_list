from django.http import HttpResponse #(lets u use python in django)
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #python lets u pass any arguements and key arguements, its requesting a url for something(which is here html content)
    #return HttpResponse ("<h1>Hello world</h1>") #string of html code
    return render(request, "home.html", {}) # to render the above and for it create a template folder

def contact_view(request, *args, **kwargs): #python lets u pass any arguements and key arguements
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): #python lets u pass any arguements and key arguements
    return render(request, "about.html", {})
