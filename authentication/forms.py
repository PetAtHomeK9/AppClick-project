from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=20, required=True, 
              widget=forms.TextInput({"placeholder":'First name'})
              )
    last_name=forms.CharField(max_length=20, required=True,
              widget=forms.TextInput({'placeholder':'Last name'})
              )
    email=forms.EmailField(max_length=30, required=True, 
              widget=forms.TextInput({'placeholder':'Email'})
              )
    username=forms.CharField(max_length=20,required=True, 
              widget=forms.TextInput({'placeholder':'Username'})
              )
    password1=forms.CharField(min_length=8,required=True,
              widget=forms.PasswordInput({'placeholder':'Password'})
              )
    password2=forms.CharField(min_length=8,required=True,
              widget=forms.PasswordInput({'placeholder':'Confirm Password'})
              )
    class Meta:
        model= User
        fields= ('first_name','last_name','email','username','password1','password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label=None, required=True, widget=forms.TextInput({"placeholder" : "Enter your username"}))
    password=forms.CharField(min_length=8, label= None,required=True, widget=forms.PasswordInput({"placeholder": "Enter your password"}))

class ChangePasswordForm(PasswordChangeForm):
    old_password=forms.CharField(min_length=8, widget=forms.PasswordInput({'placeholder':'Old Password:'}))
    new_password1=forms.CharField(min_length=8, widget=forms.PasswordInput({'placeholder':'New Password:'}))
    new_password2=forms.CharField(min_length=8, widget=forms.PasswordInput({'placeholder':'Confirm Password:'}))