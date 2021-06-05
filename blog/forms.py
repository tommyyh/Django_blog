from django import forms

class PostForm(forms.Form):
  headline = forms.CharField(max_length=150)
  content = forms.CharField(widget=forms.Textarea)