from django.urls import path
from rest_framework import views
from .views import *

app_name = 'mypage'

urlpatterns = [
    path('mypage', MyPageView.as_view(), name='mypage'),
    path('mypage/my-favorite', MyFavoriteView.as_view(), name='myfavorite'),
    path('mypage/<int:user_id>', UserDeleteView.as_view()),
]