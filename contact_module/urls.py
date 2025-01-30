from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact_us_view'),
    path('create-profile', views.CreateProfileView.as_view(), name='create_profile_view'),
]
