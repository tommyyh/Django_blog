from django.urls import path
from . import views

urlpatterns = [
  path('', views.account, name='account'),
  path('register/', views.register, name='account-register'),
  path('login/', views.login, name='account-login'),
]