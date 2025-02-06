from django.urls import path
from . import views

urlpatterns = [
    path("user-dashboard", views.user_dashboard.as_view(), name="user-dashboard"),
    path("change-password", views.ChangePasswordView.as_view(), name="change-password"),
    path("edit-profile", views.editUserProfile.as_view(), name="edit-profile"),
]
