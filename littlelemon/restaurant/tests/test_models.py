from django.test import TestCase
from restaurant.models import Menu, BookingTable

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price = 80, inventory = 100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_create_item(self):
        menuItem = Menu.objects.create(
            title="Pancakes",
            price= 240,
            inventory= 40
        )
        self.assertEqual(str(menuItem), "Pancakes : 240")
