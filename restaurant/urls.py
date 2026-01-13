"""
URL routing configuration for the restaurant application.

Defines all URL patterns for the restaurant app including
home page, menu API endpoints, booking management, and authentication.
"""
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

# Initialize router for booking viewset
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    # Home page route
    path('', views.index, name='index'),
    
    # Menu API endpoints
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    
    # Booking management (via router)
    path('booking/', include(router.urls)),
    
    # Authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
