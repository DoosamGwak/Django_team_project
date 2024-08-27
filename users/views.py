
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST,require_http_methods
from .forms import ProfileImageForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.'
@login_required
@require_http_methods(["GET","POST"])
def profile(request, username):
    if username=='AnonymousUser':
        username=request.user.username
    member = get_object_or_404(get_user_model(), username=username)
    profile_image = Profile.objects.filter(user=member).last()

    if request.method == "POST":
        form = ProfileImageForm(request.POST, request.FILES, instance=profile_image)
        if form.is_valid():
            profile_image = form.save(commit=False)
            profile_image.user = member
            profile_image.save()
            return redirect("users:profile", username=member.username)
    else:
        form = ProfileImageForm(instance=profile_image)

    context = {
        "member": member,
        "date_joined": member.date_joined,
        "form": form,
        "profile_image": profile_image,
    }
    return render(request, "users/profile.html", context)


def reset_profile_image(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    profile_image = Profile.objects.filter(user=member).last()

    if request.user == member and profile_image:
        profile_image.image.delete()
        profile_image.image = None
        profile_image.save()
    return redirect('users:profile', username=member.username)



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