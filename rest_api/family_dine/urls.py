from django.urls import path
from .views import *


app_name = "family_dine"  # for reverse namespace
urlpatterns = [
    path('', DineList.as_view(), name='dine-list'),
    path('list/<username>/', UserDineList.as_view(), name='user-dine-list'),
    path('detail/<int:pk>/', DineDetail.as_view(), name='dine-detail'),
    path('locations/', DineLocationList.as_view(), name='dine-location-list'),
    path('join-dine/<int:pk>/', JoinDine.as_view(), name='join-dine')
]

