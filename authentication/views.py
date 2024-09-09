from django.shortcuts import render, get_object_or_404,redirect
from .models import User
from .forms import SignupForm,LoginForm, ChangePasswordForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
# Create your views here.




def log_in(request):
    if request.method=='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(request, username=username,password=password)
            if user != None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid Username or Password')
                

    else:
        form=LoginForm()
    
    return render(request, 'login.html', {'form':form})

    
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            context = {
                'form':form
            }
            return render(request, 'signup.html', context)

    else:
        form= SignupForm()
        context = {
            'form':form
        }
    return render(request, 'signup.html', context)
@login_required
def log_out(request):
    pass
@login_required
def profile(request):
    user= request.user
    context={
        'user':user
    }
    return render(request, 'profile.html', context)

class ChangePasswordView(PasswordChangeView):
    form_class= ChangePasswordForm
    template_name='change_password.html'
    success_url='done/'