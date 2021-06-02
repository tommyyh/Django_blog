from django.shortcuts import render

# Views
def home(request):
  return render(request, 'blog/home.html')