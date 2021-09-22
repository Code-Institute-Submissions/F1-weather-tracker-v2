from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_premium, name='buy_premium'),
    path('charge/', views.charge, name="charge"),
    path('success/', views.successMsg, name="success"),
]
