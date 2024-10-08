from django.contrib import admin
from django.urls import path
from shop import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('dog_details/<int:dog_id>/', views.dog_details, name='dog_details'),
    path('place_order/<int:dog_id>/', views.place_order, name='place_order'),
    path('order_details/<int:order_id>/', views.order_detail, name='order_details'),
    path('search/', views.search, name='search_results'),


]


