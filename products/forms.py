from .models import Product, Comment
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['author','clicked',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'