from django.urls import path
from .views import log_in,sign_up



urlpatterns = [
    path('', log_in, name='log_in'),
    path('sign_up/', sign_up, name='sign_up'),
]