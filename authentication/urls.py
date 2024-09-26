from django.urls import path
from .views import log_in,sign_up,log_out,profile,ChangePasswordView,status_delivered,add_dogs,browse_dogs,handle_listings,update_profile,edit_dog,delete_dog
from django.contrib.auth.views import PasswordChangeDoneView



urlpatterns = [
    path('', log_in, name='log_in'),
    path('profile/', profile, name='profile'),
    path('signup/', sign_up, name='sign_up'),
    path('log_out/', log_out, name='log_out'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('change-password/done/', PasswordChangeDoneView.as_view(template_name='password_changed.html'), name='password-changed'),
    path('order/<int:order_id>/status_delivered/', status_delivered, name='status_delivered'),
    path('add_dogs/', add_dogs, name='adding_dogs'),
    path('handle_listings/', handle_listings, name='handle_listings'),
    path('handle_listings/browse/', browse_dogs, name='browse_dogs'),
    path('add_profile/', update_profile, name='add_profile'),
    path('handle_listings/edit/<int:dog_id>/', edit_dog, name='edit_dog'),
    path('handle_listings/delete/<int:dog_id>/',delete_dog, name='delete_dog')

]


