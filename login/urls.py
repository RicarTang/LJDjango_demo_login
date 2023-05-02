from django.urls import path
from login import views


urlpatterns = [
    path('login/', views.login),  # 指向views视图文件的视图函数
    path('index/', views.index, name="index"),
    path('register/', views.register),
    path('logout/', views.logout)
]