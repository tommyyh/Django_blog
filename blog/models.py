from django.db import models

# Models
class Post(models.Model):
  headline = models.CharField(max_length=100)
  content = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)