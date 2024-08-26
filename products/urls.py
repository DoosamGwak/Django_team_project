from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products, name='products'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('like/<int:pk>/', views.like, name='like'),
    path('hashtag/<str:hashtag_name>/', views.hashtag_detail, name='hashtag_detail')
]