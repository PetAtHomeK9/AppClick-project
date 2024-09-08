from django.urls import path
from .views import log_in,sign_up,log_out,profile



urlpatterns = [
    path('profile/', profile, name='profile'),
    path('', log_in, name='log_in'),
  
    path('signup/', sign_up, name='sign_up'),
    path('log_out/', log_out, name='log_out'),
   
 
]


