from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.db.models import Count
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required



def products(request):
    sort = request.GET.get('sort','')
    if sort == 'like':
        products = Product.objects.annotate(like_count = Count('user_like')).order_by('-like_count','-pk')
    else:
        products = Product.objects.order_by('-pk')
    context = {
        'products': products,
        'sort': sort
    }
    return render(request, 'products/products.html', context)


@login_required
@require_http_methods(["GET","POST"])
def create(request):
    if request.method == "POST":
        form= ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect("products:products")
    else:
        form = ProductForm
    context = {'form': form}
    return render(request, 'products/create.html', context)


def detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
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