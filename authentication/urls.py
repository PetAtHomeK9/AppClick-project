from django.urls import path
from .views import log_in,sign_up,log_out,profile,ChangePasswordView
from django.contrib.auth.views import PasswordChangeDoneView



urlpatterns = [
    path('profile/', profile, name='profile'),
    path('', log_in, name='log_in'),
    path('signup/', sign_up, name='sign_up'),
    path('log_out/', log_out, name='log_out'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('change-password/done/', PasswordChangeDoneView.as_view(template_name='password_changed.html'), name='password-changed'),
   

]


