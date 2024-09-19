from django.shortcuts import render,redirect
from shop.models import Dog,SellerProfile,Order
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
                
                if user.roles=='seller':
                    return redirect('index')
                else:
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
            return redirect('log_in')
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
    logout(request)
    return redirect('index')






@login_required
def profile(request):
    user= request.user
    dogs= None
    order=None
    acc_balance=1000
    seller_profile=None
    if user.roles=='seller':
        seller_profile= SellerProfile.objects.get(user=user)
        dogs=Dog.objects.filter(user=user)
        sales=Order.objects.filter(dog__user=user)
        order= Order.objects.filter(buyer=user)
        acc_balance=sum(sale.total_price for sale in sales)
    
    elif user.roles=='buyer':
        order = Order.objects.filter(buyer=user)

    context={
        'user':user,
        'seller_profile':seller_profile,
        'order':order,
        'acc_balance':acc_balance,
        'dogs': dogs
    }
    return render(request, 'profile.html', context)

class ChangePasswordView(PasswordChangeView):
    form_class= ChangePasswordForm
    template_name='change_password.html'
    success_url='change-password/done/'