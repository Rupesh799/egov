from django.urls import path
from Home import views

urlpatterns = [
    path('', views.Home , name="Home"),
    path('alert/', views.alert , name="alert"),
   
    
]
