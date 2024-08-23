from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from django.contrib.auth import get_user_model


# Create your views here.
def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = { 'member' : member }
    return render(request, 'users/profile.html', context)