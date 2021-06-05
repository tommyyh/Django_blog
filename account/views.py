from django.shortcuts import render, redirect
from .forms import Register
from .models import Account
import bcrypt

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
        password = hashed_password,
      )

      new_account.save()
      return redirect('blog-home')

  return render(request, 'account/register.html', { 'forms': Register })