from django.shortcuts import render
from .models import Product
# Create your views here.
def product_detail_view(request): #keep the functions lower case and diff from the class
    obj = Product.objects.get(id=2)
      #  context ={
      #      'title' : obj.title,
      #      'description' : obj.description
       # }
    context = {
       'object' : obj
       }
    return render(request, "product/detail.html", context)
