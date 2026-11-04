from django.urls import path
from . import views

urlpatterns = [
   
    path('success/', views.success_page, name='success_page'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),

]