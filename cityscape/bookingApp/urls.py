from django.urls import path
from bookingApp import views

urlpatterns = [
    path('vacancylist/', views.vacany_list, name='vacancylist'),
    path('reservation/', views.reservation, name='reservation')
]