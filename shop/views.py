from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Dog, Order, SellerProfile
from .forms import DogForm

def index(request):
    dogs = Dog.objects.all()
    return render(request, 'index.html', {'dogs': dogs})


def search(request):
    query = request.GET.get('q', '')
    sex = request.GET.get('sex', '')
    age = request.GET.get('age', '')

    dogs = Dog.objects.all()

    if query:
        dogs = dogs.filter(breed__icontains=query)
    
    if sex:
        dogs = dogs.filter(gender=sex)
    
    if age:
        dogs = dogs.filter(age__lte=age)
    
    context = {
        'dogs': dogs,
        'query': query,
        'sex': sex,
        'age': age
    }
    
    return render(request, 'search_results.html', context)

def dog_details(request, dog_id):
    dog = Dog.objects.filter(id=dog_id).first()
    if not dog or not dog.availability:
        return render(request, 'not_available.html', {'dog_id': dog_id})  # Create a template for unavailable dogs
    return render(request, 'dog_details.html', {'dog': dog})



@login_required
def place_order(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id, availability=True)

    if request.method == 'POST':
        # Check if the user has enough balance
        if request.user.account_balance >= dog.price:
            # Create the order
            order = Order.objects.create(
                dog=dog,
                buyer=request.user,
                total_price=dog.price
            )
            # Deduct the amount from user's balance
            request.user.account_balance -= dog.price
            request.user.save()

            # Mark the dog as not available
            dog.availability = False
            dog.save()

            # Redirect to the order detail page
            return redirect('order_details', order_id=order.id)
        else:
            # Handle insufficient balance
            return render(request, 'insufficient_balance.html')  # Create this template to inform users

    return render(request, 'place_order.html', {'dog': dog})



@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_details.html', {'order': order})




@login_required
def sell_dog(request):
    # Check if the logged-in user is a seller
    if request.user.roles != 'seller':
        return redirect('home')  # Redirect to home if not a seller
    
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)  # Include file uploads for dog images
        if form.is_valid():
            dog = form.save(commit=False)
            dog.user = request.user  # Link the dog to the user posting it
            dog.save()
            return redirect('dog_list')  # Redirect to a list showing all posted dogs
    else:
        form = DogForm()

    return render(request, 'sell_dog.html', {'form': form})




@login_required
def profile_view(request):
    user = request.user
    seller_profile = getattr(user, 'sellerprofile', None)  # Get seller profile if it exists
    context = {
        'user': user,
        'seller_profile': seller_profile,
        'account_balance': user.account_balance,
    }
    return render(request, 'profile.html', context)
