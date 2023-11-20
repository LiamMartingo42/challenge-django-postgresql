from django.urls import path
from .views import login, signin, logout
from product.urls import urlpatterns

urlpatterns = [
    urlpatterns[1],    
    path('login',login,name='login'),
    path('sign-in',signin, name='signin'),
    path('logout',logout,name="logout")
] 