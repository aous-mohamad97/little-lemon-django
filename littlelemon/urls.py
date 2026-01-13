"""
Main URL configuration for the Little Lemon Django project.

This module defines the root URL patterns and includes
URL configurations from the restaurant app and authentication.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Restaurant application routes
    path('api/', include('restaurant.urls')),
    
    # User authentication endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
