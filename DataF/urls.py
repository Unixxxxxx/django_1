from django.urls import path
from .views import data_view, success_view

urlpatterns = [
    path('data/', data_view, name='data'),
    path('success/', success_view, name='success'),
]

