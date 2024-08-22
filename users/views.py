from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST


# Create your views here.
def users(request):
    return render(request, "users/users.html")

def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        "member": member,
        "date_joined": member.date_joined,
        }
    return render(request, "users/profile.html", context)


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), id=user_id)
        if request.user != member:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", username=member.username)
    return redirect("account:login")