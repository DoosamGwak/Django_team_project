from .models import Product, Comment, HashTag
from django import forms
import re

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['author','clicked','hashtag',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'