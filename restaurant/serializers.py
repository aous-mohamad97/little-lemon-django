"""
Serializers for converting model instances to JSON and vice versa.

This module provides serializers for menu items, bookings, and user management.
"""
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Booking, Menu


class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer for Menu model.
    
    Converts Menu instances to JSON format for API responses
    and validates incoming data for menu item creation/updates.
    """
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        read_only_fields = ['id']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    
    Handles serialization of booking data including customer name,
    number of guests, and reservation date/time.
    """
    class Meta:
        model = Booking
        fields = '__all__'


class GroupNameField(serializers.RelatedField):
    """
    Custom field serializer for Group model.
    
    Returns only the group name instead of the full group object.
    """
    def to_representation(self, value):
        """Return the name of the group."""
        return value.name


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model with group information.
    
    Includes user details along with associated group names.
    """
    groups = GroupNameField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')