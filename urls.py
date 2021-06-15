from django.urls import path,include

urlpatterns = [
    path('', views.index),
    path('/user',views.user_name),
    path('/userlists',views.register),
]