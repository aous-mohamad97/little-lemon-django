"""
View definitions for the restaurant application.

This module contains both template-based views for rendering HTML pages
and API views for handling menu items and booking operations.
"""
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


def index(request):
    """
    Render the home page template.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered HTML template for the home page
    """
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    """
    API endpoint for listing all menu items and creating new ones.
    
    Supports GET (list all items) and POST (create new item) operations.
    Requires authentication to access.
    """
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, or deleting a specific menu item.
    
    Supports GET (retrieve), PUT/PATCH (update), and DELETE operations.
    Requires authentication to access.
    """
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing restaurant table bookings.
    
    Provides full CRUD operations (Create, Read, Update, Delete) for bookings.
    Requires authentication to access.
    """
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer