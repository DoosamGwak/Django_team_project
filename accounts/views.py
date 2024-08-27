from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_http_methods, require_POST



@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:  # 비로그인 상태에서만 url로 접근 가능
        return redirect("products:products")
    if request.method == "POST": #내가 데이터를 치고 들어온것
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_path = request.GET.get("next") or 'products:products'
        return redirect(next_path)
    else: #url 내가 직접 치고온거 or <a href=''></a>
        form = AuthenticationForm()
    context = { "form": form }  
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('products:products')


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":   #내가 데이터를 치고 들어온것
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():     #폼 유효성 검사
            user = form.save()
            auth_login(request, user)   #로그인, 세션만들기V
        return redirect('products:products')
    else:     #url 내가 직접 치고온거 or <a href=''></a>
        form = CustomUserCreationForm()   #데이터를 입력하는창
    context = {'form': form }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(["GET","POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("products:products")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, 'accounts/update.html', context)


@require_http_methods(["GET","POST"])
def update_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) 
            return redirect('products:products')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request,'accounts/update_password.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('products:products')