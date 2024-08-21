from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.
def users(request):
    return render(request, "users/users.html")

def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        "member": member,
        }
    return render(request, "users/profile.html", context)