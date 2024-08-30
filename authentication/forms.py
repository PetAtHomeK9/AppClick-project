from django import forms
from .models import User # Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=20, required=True, help_text='First name')
    last_name=forms.CharField(max_length=20, required=True, help_text='Last name')
    email=forms.EmailField(max_length=30, required=True, help_text='Email')

    class Meta:
        model= User
        fields= ('first_name','last_name','email','username','password1','password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label=None, required=True, widget=forms.TextInput({"placeholder" : "Enter your username"}))
    password=forms.CharField(min_length=8, label= None,required=True, widget=forms.PasswordInput({"placeholder": "Enter your password"}))

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields= ['bio','profile_img','location','birth_date']

#         widgets={
#             'birth_date': forms.DateInput(attrs={'type': 'date'})
#         }


        