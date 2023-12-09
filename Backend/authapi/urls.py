from django.urls import path
from .views import*

app_name = "authapi"

urlpatterns = [
    path('register', UserRegistration, name = 'register'),
    path('login', UserLogin, name = 'login'),
    path('profile', UserProfile, name = 'profile'),
    path('changepassword', ChangePassword, name = 'changepassword'),
    path('sendresetpasswordemail',  SendPasswordResetEmail, name = 'sendresetpasswordemail'),
    path('resetpassword/<uid>/<token>', ResetPassword, name = 'resetpassword'),
]
