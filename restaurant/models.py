"""
Database models for the restaurant application.

This module defines the data models for menu items and customer bookings.
"""
from django.db import models


class Menu(models.Model):
    """
    Represents a menu item available at the restaurant.
    
    Attributes:
        title: Name of the menu item
        price: Price of the item in decimal format
        inventory: Current stock quantity available
    """
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
        ordering = ['title']

    def __str__(self) -> str:
        """Return a string representation of the menu item."""
        return f'{self.title} - ${self.price}'

    def is_available(self) -> bool:
        """Check if the menu item is currently in stock."""
        return self.inventory > 0


class Booking(models.Model):
    """
    Represents a table reservation at the restaurant.
    
    Attributes:
        name: Name of the person making the reservation
        number_of_guests: Number of people in the party
        booking_date: Date and time of the reservation
    """
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(default=6)
    booking_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ['booking_date']

    def __str__(self) -> str:
        """Return a string representation of the booking."""
        return f'{self.name} - {self.number_of_guests} guests on {self.booking_date.strftime("%Y-%m-%d %H:%M")}'