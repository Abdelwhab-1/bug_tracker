from django.urls import path, include 
from .views import (SignUp, Index)
from django.contrib.auth.views import LoginView
app_name = 'authinticator'
urlpatterns = [
    path('home', Index.as_view(), name='home'), 
    path('register/', SignUp.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'), 
    path('accounts/', include('django.contrib.auth.urls',)), 
    
]