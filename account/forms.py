from django import forms

class Register(forms.Form):
  email = forms.CharField(
    label='',
    max_length=150,
    widget = forms.EmailInput(attrs={ 'placeholder': 'Email Address' })
  )
  username = forms.CharField(
    label='',
    max_length=150,
    widget = forms.TextInput(attrs={ 'placeholder': 'Username' })
  )
  password = forms.CharField(
    label='',
    max_length=150,
    widget = forms.PasswordInput(attrs={ 'placeholder': 'Password' })
  )