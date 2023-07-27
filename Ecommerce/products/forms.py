from django import forms

from Ecommerce.products.models import Product


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search by Product Name')


class ProductForm(forms.ModelForm):
    photo = forms.ImageField(label='Product Image', required=False)

    class Meta:
        model = Product
        fields = ['photo', 'name', 'description', 'quantity', 'brand', 'made_in', 'price', 'category']