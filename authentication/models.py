from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_img = models.FileField(upload_to="profile", default=None)
    account_balance = models.DecimalField(default=100000,max_digits=1000000000, decimal_places=2)

    USER_OPTIONS= (
        ('seller','Seller'),
        ('buyer','Buyer')
    )
    role = models.CharField(max_length=10, choices=USER_OPTIONS, default='seller')