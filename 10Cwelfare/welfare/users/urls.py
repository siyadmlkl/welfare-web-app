from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('logIn',views.logIn),
    path('logOut',views.logOut),
]