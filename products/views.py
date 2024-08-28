from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, HashTag
from django.db.models import Count
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.http import JsonResponse
from users.models import Profile


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




@login_required
@require_http_methods(["GET","POST"])
def create(request):
    if request.method == "POST":
        form= ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            # hashtags = re.findall(r'#(\w+)', product.content)
            # for tag in hashtags:
            #     hashtag, _ = HashTag.objects.get_or_create(hashtag_name=tag)
            #     product.hashtag.add(hashtag)
            product.save_hash()

            return redirect("products:products")
    else:
        form = ProductForm
    context = {'form': form}
    return render(request, 'products/create.html', context)


def detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    product.clicked += 1
    product.save()
    profile=Profile.objects.get(user=product.author)

    context = {
        'product': product,
        'profile': profile
    }
    return render(request,'products/detail.html', context)


@require_http_methods(["GET", "POST"])
def update(request,pk):
    product= get_object_or_404(Product,pk=pk)
    if product.author != request.user:
        return redirect('products:detail',pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save(commit=False)
            product.save_hash()
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


@login_required
@require_POST
def like(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.user_like.filter(pk=request.user.pk).exists(): 
        product.user_like.remove(request.user)
        liked = False 
    else:
        product.user_like.add(request.user)
        liked = True
    context = {
        'liked': liked,
        'count': product.user_like.count()
    }
    return JsonResponse(context)


def hashtag_detail(request, hashtag_name):
    hashtag = get_object_or_404(HashTag, hashtag_name=hashtag_name)
    products = Product.objects.filter(hashtag=hashtag)
    context = {
        'hashtag': hashtag,
        'products': products,
        }
    return render(request, 'products/hashtag.html', context)