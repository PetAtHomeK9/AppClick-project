from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dog, Order, SellerProfile

def index(request):
    dogs = Dog.objects.all()
    return render(request, 'index.html', {'dogs': dogs})


def dog_details(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id, availability=True)

    return render(request, 'dog_details.html', {'dog': dog})

@login_required
def place_order(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id, availability=True)
    
    if request.method == 'POST':
        # Create the order
        order = Order.objects.create(
            dog=dog,
            buyer=request.user,
            total_price=dog.price
        )
        dog.availability = False
        dog.save()
        
        # Redirect to the order detail page
        return redirect('order_detail', order_id=order.id)
    
    return render(request, 'place_order.html', {'dog': dog})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

