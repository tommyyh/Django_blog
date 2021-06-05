from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post
from django.utils.decorators import decorator_from_middleware
from account.middlewares import Authenticate
from account.models import Account

# Views
def home(request):
  posts = Post.objects.all()

  return render(request, 'blog/home.html', { 'posts': posts })

@decorator_from_middleware(Authenticate)
def new_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    author = Account(id=7)

    if form.is_valid():
      add_post = Post(
        headline = form.cleaned_data['headline'],
        content = form.cleaned_data['content'],
        author = author
      )

      add_post.save()

      return redirect('blog-home')

  return render(request, 'blog/new_post.html', { 'form': PostForm })