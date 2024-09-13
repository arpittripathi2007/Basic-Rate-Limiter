from django.contrib import admin
from django.urls import path, include
from handlers import views

urlpatterns = [
    path('journey/', views.Journey.as_view(), name='journey'),
    path('boundary/', views.Boundary.as_view(), name='boundary'),
    path('journey/reset', views.ResetJourney.as_view(), name='journey_reset'),
    path('boundary/reset', views.ResetBoundary.as_view(), name='boundary_reset'),
    path('clear', views.clear_cache, name='clear_cache'),
    path('users', views.ListUsers.as_view(), name='users_api'),
    path('register', views.RegisterView.as_view(), name='auth_register'),
]
