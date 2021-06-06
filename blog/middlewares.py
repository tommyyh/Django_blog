from .models import Post
from django.shortcuts import redirect

# Allow access to post for only the author
class Authorize():
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)

    return response

  def process_view(self, request, view_func, view_args, view_kwargs):
    # Get the post id
    post_id = view_kwargs.get('id', None)
    user_id = request.session['user'].get('id')
    post = Post.objects.get(id = post_id)

    if post.author_id == user_id:
      return
    else:
      return redirect('blog-home')
