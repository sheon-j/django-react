from django.shortcuts import render
from .models import Post

# Function Based View
def post_list(request):
  queryset = Post.objects.all()
  return render(request, 'blog/post_list.html', {
    'posts': queryset,
  })