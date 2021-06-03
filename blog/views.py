from django.shortcuts import render

# Views
def home(request):
  posts = ['post1', 'post2', 'post3', 'post4']

  return render(request, 'blog/home.html')