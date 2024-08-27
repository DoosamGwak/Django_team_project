
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from .forms import ProfileImageForm
from .models import Profile
from django.utils import timezone   # 상점 오픈일 계산 관련 


# Create your views here.

def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    profile_image = Profile.objects.filter(user=member).last()

    # 필요한 데이터를 미리 가져옴
    liked_products = member.product_like.all()  # 사용자가 좋아요를 누른 게시물
    following_list = member.followings.all()  # 사용자가 팔로잉 중인 유저 목록
    followers_list = member.followers.all()  # 사용자를 팔로우하는 유저 목록

    # 상점 오픈일 계산
    shop_open_days = (timezone.now() - member.date_joined).days
    # 해당 프로필 유저가 찜한 게시물만 가져오기
    liked_products = member.product_like.all()

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
        "liked_products": liked_products,  # 찜한 게시물 데이터를 템플릿으로 전달
        "following_list": following_list,  # 팔로잉 유저 데이터를 템플릿으로 전달
        "followers_list": followers_list,  # 팔로워 데이터를 템플릿으로 전달
        "shop_open_days": shop_open_days,  # 상점 오픈일 데이터 템플릿으로 전달
        "liked_products": liked_products,  # 찜한 게시물 리스트
        # 기타 필요한 컨텍스트 데이터들 
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