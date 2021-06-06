from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post
from django.utils.decorators import decorator_from_middleware
from account.middlewares import Authenticate
from blog.middlewares import Authorize
from account.models import Account

# Views
def home(request):
  posts = Post.objects.all()
  user_id = request.session['user'].get('id')

  return render(request, 'blog/home.html', { 'posts': posts, 'user_id': user_id })

@decorator_from_middleware(Authenticate)
def new_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    author = Account(id = request.session['user'].get('id'))

    if form.is_valid():
      add_post = Post(
        headline = form.cleaned_data['headline'],
        content = form.cleaned_data['content'],
        author = author
      )

      add_post.save()

      return redirect('blog-home')

  return render(request, 'blog/new_post.html', { 'form': PostForm })

@decorator_from_middleware(Authenticate)
@decorator_from_middleware(Authorize)
def edit_post(request, id):
  if request.method == 'PUT':
    new_form = PostForm(request.PUT)

    if new_form.is_valid():
      form_headline = new_form.cleaned_data['headline']
      form_content = new_form.cleaned_data['content']

      # Update post
      Post.objects.filter(id = id).update(headline = form_headline, content = form_content)
      messages.success(request, 'Successfully updated your post')

      return redirect('blog-home')

  post = Post.objects.get(id = id)
  form = PostForm(initial = { 'headline': post.headline, 'content': post.content })

  return render(request, 'blog/edit.html', { 'form': form, 'post_id': post.id })

def not_found(request):
  return render(request, 'blog/404.html')