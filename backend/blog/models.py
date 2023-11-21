from django.conf import settings
from django.db import models

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  blog_url = models.URLField(blank=True)

# 피스칼 네이밍, 단수 사용
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=100, db_index=True) # db_index=True: 색인에 활용
  slug = models.SlugField(
    allow_unicode=True, # allow_unicode=True: 한글도 가능
    db_index=True
  )
  desc = models.TextField(blank=True)
  image = models.ImageField(blank=True)
  comment_count = models.PositiveIntegerField(default=0)
  tag_set = models.ManyToManyField('Tag', blank=True)
  is_published = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)
