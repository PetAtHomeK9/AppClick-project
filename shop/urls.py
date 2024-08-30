from django.contrib import admin
from django.urls import path
from shop import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('place_order/<int:dog_id>/', views.place_order, name='place_order'),
]


