
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
]
