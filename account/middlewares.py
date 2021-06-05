from django.shortcuts import redirect
import jwt
from decouple import config

class Authenticate():
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)

    return response

  def process_request(self, request):
    # Authenticate user via json web token
    if 'token' in request.COOKIES:
      # Decode the token
      try:
        token = request.COOKIES['token']
        decoded_token = jwt.decode(token, config('JWT_SECRET'), algorithms=['HS256'])

        # Save the account in the session
        request.session['user'] = decoded_token
        
        return
      except:
        return redirect('blog-home')
    else:
      return redirect('blog-home')