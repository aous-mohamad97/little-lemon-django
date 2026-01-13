"""
Unit tests for restaurant application models.

Tests cover menu item creation, inventory management,
booking creation, and default value assignments.
"""
from datetime import datetime
from decimal import Decimal

from django.test import TestCase

from restaurant.models import Booking, Menu


class MenuTest(TestCase):
    """Test cases for Menu model functionality."""

    def test_create_item(self):
        """Test creating a menu item with all fields."""
        item = Menu.objects.create(
            title="IceCream",
            price=Decimal('80'),
            inventory=100
        )
        self.assertEqual(str(item), "IceCream - $80")
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, Decimal('80'))
        self.assertEqual(item.inventory, 100)

    def test_default_inventory(self):
        """Test that default inventory value is set correctly."""
        item = Menu.objects.create(title="Cake", price=Decimal('50'))
        self.assertEqual(item.inventory, 5)

    def test_is_available(self):
        """Test the is_available method for menu items."""
        available_item = Menu.objects.create(
            title="Pizza",
            price=Decimal('25'),
            inventory=10
        )
        unavailable_item = Menu.objects.create(
            title="Burger",
            price=Decimal('15'),
            inventory=0
        )
        self.assertTrue(available_item.is_available())
        self.assertFalse(unavailable_item.is_available())


class BookingTest(TestCase):
    """Test cases for Booking model functionality."""

    def test_create_booking(self):
        """Test creating a booking with all required fields."""
        booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            booking_date=datetime(2023, 6, 24, 18, 0)
        )
        expected_str = "John Doe - 4 guests on 2023-06-24 18:00"
        self.assertEqual(str(booking), expected_str)
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.number_of_guests, 4)

    def test_default_number_of_guests(self):
        """Test that default number of guests is set correctly."""
        booking = Booking.objects.create(
            name="Jane Doe",
            booking_date=datetime(2023, 6, 24, 19, 0)
        )
        self.assertEqual(booking.number_of_guests, 6)
