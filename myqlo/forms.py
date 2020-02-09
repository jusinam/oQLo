from django import forms
from .models import Image

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='Username',max_length=30)
    email = forms.EmailField(label='Email')