from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Women
        fields = ['title', 'content', 'photo', 'is_publish', 'cat']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':60, 'rows':10}),
        }

class register_form(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class login_form(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='name', min_length=2)
    email = forms.EmailField(label='email', max_length=100)
    content = forms.CharField(label='text', widget=forms.Textarea(attrs={
        'cols':60,
        'rows':10
    }))
    captcha = CaptchaField()

