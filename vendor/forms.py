from django.forms import ModelForm

from product.models import Product, ProductImage


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description',
                  'price', 'image', 'thumbnail']


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
