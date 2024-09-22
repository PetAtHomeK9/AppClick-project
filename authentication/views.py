from django.shortcuts import render,redirect,get_object_or_404
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
                
                if user.role=='seller':
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
            if user.role=='seller':
                SellerProfile.objects.create(user=user)
                

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
    acc_balance=1000
    seller_profile=None
    if user.role=='seller':
        seller_profile= SellerProfile.objects.filter(user=user).first()
        if seller_profile:
           dogs=Dog.objects.filter(user=user)
           orders =Order.objects.filter(dog__user=user)
           acc_balance=sum(order.total_price for order in orders)

        else:
            seller_profile = SellerProfile.objects.create(user=user)
            
    
    else:
           orders = Order.objects.filter(buyer=user)

    context={
        'user':user,
        'seller_profile':seller_profile,
        'orders':orders,
        'acc_balance':acc_balance,
        'dogs': dogs
    }
    return render(request, 'profile.html', context)

class ChangePasswordView(PasswordChangeView):
    form_class= ChangePasswordForm
    template_name='change_password.html'
    success_url='change-password/done/'


@login_required
def status_delivered(request, order_id):
    user = request.user
    order= get_object_or_404(Order, id=order_id)

    if order.dog.user == user:
        order.status = 'Delivered'
        order.save()
        return redirect('profile')
    
    else:
        return redirect('profile')
    

def add_dogs(request):
    if request.method=='POST':
        pass
    return render(request, 'adding_dogs.html')


@login_required
def handle_listings(request):
    dogs = Dog.objects.filter(user=request.user)
    context={
        'dogs':dogs
    }
    return render(request, 'handle_listings.html', context)

def browse_dogs(request):
    dogs= Dog.objects.filter(availability=True)
    context={
        'dogs':dogs
    }
    return render(request, 'browsing_dogs.html', context)