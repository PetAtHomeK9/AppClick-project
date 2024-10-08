from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Dog,SellerProfile,Order
from .forms import SignupForm,LoginForm, ChangePasswordForm,DogForm,ProfileForm
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
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if 'profile_img' in request.FILES:
                user.profile_img=request.FILES['profile_img']
            user.save()
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user.role=='seller':
                SellerProfile.objects.create(user=user)
                

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
    return render(request, 'authentication/profile.html', context)

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
    if request.user.role=='seller':
       if request.method=='POST':
           form = DogForm(request.POST, request.FILES)
           if form.is_valid():
               dog = form.save(commit=False)
               dog.user = request.user
               dog.save()
               return redirect('handle_listings')
       else:
               form = DogForm()
    
       return render(request, 'authentication/adding_dogs.html', {'form':form})
    else:
        return redirect('profile')


@login_required
def handle_listings(request):
    dogs = Dog.objects.filter(user=request.user)
    context={
        'dogs':dogs
    }
    return render(request, 'authentication/Manage_listings.html', context)

def browse_dogs(request):
    dogs= Dog.objects.filter(availability=True)
    context={
        'dogs':dogs
    }
    return render(request, 'authentication/browse_dogs.html', context)

def update_profile(request):
    user=request.user
    message= None

    if request.user.role=='seller':
       seller=SellerProfile.objects.filter(user=user).first()
       if request.method=='POST':
      
           form = ProfileForm(request.POST, request.FILES, instance=seller)
           if form.is_valid():
              profile=form.save(commit=False)
              profile.user=user
              profile.save()

           message = 'Updated profile successfully!'
       else:
           form = ProfileForm(instance=seller)
       context={
               'user':user,
               'seller':seller,
               'form':form,
               'message':message
           }
       return render(request, 'authentication/seller_profile.html', context)
    return redirect('profile')

def edit_dog(request, dog_id):
    dog= get_object_or_404(Dog, id=dog_id, user=request.user)
    if request.method=='POST':
        form= DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()       
            return redirect('handle_listings')
        
        else:

            context={
            'form':form,
            'dog':dog
        }

    else:
        form=DogForm(instance=dog)
        context={
            'form':form,
            'dog':dog
        }      

    return render(request, 'authentication/edit_dogs.html', context)    

def delete_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id, user=request.user)
    if request.method=='POST':
        dog.delete()
        return redirect('handle_listings')
    return render(request, 'authentication/delete_dogs.html', {'dog':dog})

def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)

    return render(request, 'authentication/dog_details.html',{'dog':dog})