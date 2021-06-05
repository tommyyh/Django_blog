from django.shortcuts import render, redirect
from .forms import Register, Login
from .models import Account
from django.contrib import messages
import bcrypt
import jwt
from decouple import config
from django.utils.decorators import decorator_from_middleware
from .middlewares import Authenticate

# Views
def register(request):
  if request.method == 'POST':
    form = Register(request.POST)

    if form.is_valid():
      # Hash password
      raw_password = bytes(form.cleaned_data['password'], encoding='utf-8')
      hashed_password = bcrypt.hashpw(raw_password, bcrypt.gensalt())
      
      # Save the user
      new_account = Account(
        email = form.cleaned_data['email'],
        username = form.cleaned_data['username'],
        password = hashed_password.decode('utf-8'),
      )

      new_account.save()
      messages.success(request, 'Account created successfully')

      return redirect('blog-home')

  return render(request, 'account/register.html', { 'forms': Register })

def login(request):
  if request.method == 'POST':
    form = Login(request.POST)

    if form.is_valid():
      account = Account.objects.filter(email = form.cleaned_data['email']).first()
      password = bytes(form.cleaned_data['password'], encoding='utf-8')

      # Check if user exists
      if not account:
        messages.error(request, 'Incorrect email address')

        return redirect('account-login')

      # Check if passwords match
      if bcrypt.checkpw(password, bytes(account.password, encoding='utf-8')):
        payload = {
          'email': account.email,
          'username': account.username, 
          'id': account.id 
        }
        encoded_jwt = jwt.encode(payload, config('JWT_SECRET'), algorithm='HS256')
        response = redirect('blog-home')
        response.set_cookie('token', encoded_jwt, max_age=None)

        messages.success(request, 'Successfully logged in')
        
        return response
      else:
        messages.error(request, 'Incorrect password')

        return redirect('account-login')


  return render(request, 'account/login.html', { 'forms': Login })

@decorator_from_middleware(Authenticate)
def account(request):
  return render(request, 'account/account.html', { 'account': request.session['user'] })