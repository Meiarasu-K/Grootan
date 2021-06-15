from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groot/',views.loginreg),
    path('groot/user/',views.user_name),
    path('groot/userlists/',views.register),
]
