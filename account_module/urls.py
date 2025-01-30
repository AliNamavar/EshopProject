from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('forgot-password/', views.forgot_passwordView.as_view(), name='forgot_password'),
    path('confirm-forgot-password/<confirmation_code>', views.forgot_passwordConfirmView.as_view(), name='confirm_forgot_password'),
    path('activate/<email_activate_code>', views.activate_accountView.as_view(), name='activate_account')
]