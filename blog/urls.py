from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='blog-home'),
  path('new-post/', views.new_post, name='blog-new'),
  path('edit-post/<int:id>', views.edit_post, name='blog-edit'),
]