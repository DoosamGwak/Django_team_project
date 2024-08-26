from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, HashTag
from django.db.models import Count
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
import re


def products(request):
    query = request.GET.get('q','')
    sort = request.GET.get('sort','')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query) |
            Q(hashtag__hashtag_name__icontains=query)
        ).distinct()

    if sort == 'like':
        products = products.annotate(like_count = Count('user_like')).order_by('-like_count','-pk')
    elif sort == 'clicked':
        products = products.order_by('-clicked','-pk')
    else:
        products = products.order_by('-pk')
        
    context = {
        'products': products,
        'sort': sort,
        'query': query
    }
    return render(request, 'products/products.html', context)


def convert_hashtags_to_links(content):
    # 해시태그를 추출하고 링크로 변환
    return re.sub(r'#(\w+)', r'<a href="/products/hashtag/\1/">#\1</a>', content)


@login_required
@require_http_methods(["GET","POST"])
def create(request):
    if request.method == "POST":
        form= ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            
            hashtags = re.findall(r'#(\w+)', product.content)
            product.content = convert_hashtags_to_links(product.content)  # 해시태그를 링크로 변환
            product.save()
            for tag in hashtags:
                hashtag, _ = HashTag.objects.get_or_create(hashtag_name=tag)
                product.hashtag.add(hashtag)

            return redirect("products:products")
    else:
        form = ProductForm
    context = {'form': form}
    return render(request, 'products/create.html', context)


def detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    product.clicked += 1
    product.save()
    context = {'product': product}
    return render(request,'products/detail.html', context)


@require_http_methods(["GET", "POST"])
def update(request,pk):
    product= get_object_or_404(Product,pk=pk)
    if product.author != request.user:
        return redirect('products:detail',pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('products:detail', pk)
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'products/update.html', context)


@require_POST
def delete(request,pk):
    product = Product.objects.get(pk=pk)
    if product.author == request.user:
        product.delete()
    return redirect('products:products')


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.user_like.filter(pk=request.user.pk).exists(): 
            product.user_like.remove(request.user) 
        else:
            product.user_like.add(request.user)
    else:
        redirect('accounts:login')
    return redirect('products:products')


def hashtag_detail(request, hashtag_name):
    hashtag = get_object_or_404(HashTag, hashtag_name=hashtag_name)
    products = Product.objects.filter(hashtag=hashtag)
    context = {
        'hashtag': hashtag,
        'products': products,
        }
    return render(request, 'products/hashtag.html', context)