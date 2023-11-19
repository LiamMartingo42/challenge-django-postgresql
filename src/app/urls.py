from django.urls import path
from app.views import index, login

urlpatterns = [
    path('',index),
    path('home/',index, name='home')
]