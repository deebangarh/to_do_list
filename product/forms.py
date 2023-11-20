from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =[
            'title' ,
            'description',
            'price'
        ]

#standard django form
class RawProductForm(forms.Form):

  title = forms.CharField()
  description = forms.CharField()
  price = forms.DecimalField()
