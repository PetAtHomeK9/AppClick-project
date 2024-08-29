from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_img = models.FileField(upload_to="profiles", default=None)

