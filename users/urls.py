from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path("", views.users, name="users"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("progile/<str:username>/reset_image/", views.reset_profile_image, name="reset_profile_image"),
    path("follow/<int:user_id>/", views.follow, name="follow"),
]