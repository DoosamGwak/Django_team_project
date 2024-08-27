from .models import Product, Comment
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['author','clicked','hashtag',]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'상품명'}),
            'content': forms.Textarea(attrs={'placeholder':'내용을 입력해주세요.'}),
        }
        labels = {
            'title': '상품명',
            'content': '내용',
            'image': '사진등록',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'