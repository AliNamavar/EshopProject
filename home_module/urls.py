from django.urls import path
from home_module import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index_home_module'),
    path('about-us', views.InfoView.as_view(), name='about_us')
]