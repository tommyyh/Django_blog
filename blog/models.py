from django.db import models
from django.shortcuts import redirect
from account.models import Account

# Models
class Post(models.Model):
  headline = models.CharField(max_length=100)
  content = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.headline