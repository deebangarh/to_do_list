from django.shortcuts import render

from .forms import ProductForm, RawProductForm #(to render the django form)

from .models import Product

def product_create_view(request): #keep the functions lower case and diff from the class
 my_form = RawProductForm(request.GET)
 if request.method == "POST":
   my_form = RawProductForm(request.POST)
 if my_form.is_valid():
    print (my_form.cleaned_data)
    Product.objects.create(**my_form.cleaned_data) #**to pass it as an arguement
 else:
     print (my_form.errors)
 context = {
       "form" : my_form
   }

 return render(request, "products/product_create.html", context)

# def product_create_view(request): #keep the functions lower case and diff from the class
#    #print(request.GET)
#    #print(request.POST)
#    if request.method == "POST":
#     my_new_title = request.POST.get('title')
#    print(my_new_title)
#    #Product.objects.create(title=my_new_title)
#    context = {}

#    return render(request, "products/product_create.html", context)


# def product_create_view(request): #keep the functions lower case and diff from the class
#     form = ProductForm(request.POST or None)

#     if form.is_valid():
#         # Save the form data to the database
#         form.save()
#         # Create a new instance of the ProductForm to clear the form
#         form = ProductForm()

#     context = {'form' : form }

#     return render(request, "products/product_create.html", context)


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
    return render(request, "products/product_detail.html", context)
