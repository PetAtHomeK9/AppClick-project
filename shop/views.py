from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dog, Order

def index(request):
    dogs = Dog.objects.all()
    return render(request, 'index.html', {'dogs': dogs})

@login_required
def place_order(request, dog_id):
    dog = Dog.objects.get(id=dog_id, availability=True)
    
    if request.method == 'POST':
        # Create the order
        order = Order.objects.create(
            dog=dog,
            buyer=request.user,
            total_price=dog.price
        )
        dog.availability = False
        dog.save()
        
        return redirect('order_detail', order_id=order.id)
    
    return render(request, 'place_order.html', {'dog': dog})
