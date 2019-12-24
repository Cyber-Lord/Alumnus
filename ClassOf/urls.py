from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="classof_home_view_url"),
]
