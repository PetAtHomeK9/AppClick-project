from django.contrib import admin
from .models import Dog, Order, SellerProfile


# Register your models here.

admin.site.register(Dog)
admin.site.register(Order)
admin.site.register(SellerProfile)
