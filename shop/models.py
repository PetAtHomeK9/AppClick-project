from django.db import models
from authentication.models import User

# Create your models here.
class Dog(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user")
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    description = models.TextField()
    display_img = models.FileField(upload_to="dog_display_img")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='seller_profiles/', blank=True, null=True)


class Order(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, default="PENDING")



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

