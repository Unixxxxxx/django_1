from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('Db/', views.Db, name='Db'),
    path('new/', views.new, name='new')
    ]
