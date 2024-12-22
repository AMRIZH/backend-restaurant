from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category, Menu

class MenuTests(TestCase):
    def setUp(self):
        # Create a Category instance
        self.category = Category.objects.create(name='Appetizers')

        # Create Menu instances
        self.menu_item_1 = Menu.objects.create(
            category=self.category,
            name='Spring Rolls',
            price=5.99,
            description='Crispy spring rolls with dipping sauce.',
            image='images/spring_rolls.jpg'
        )
        self.menu_item_2 = Menu.objects.create(
            category=self.category,
            name='Garlic Bread',
            price=3.99,
            description='Warm garlic bread with butter.',
            image='images/garlic_bread.jpg'
        )

        # Set up the API client
        self.client = APIClient()

    def test_category_view(self):
        # Test the Category API endpoint
        response = self.client.get('/api/menus/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the category is in the response data
        categories = response.json()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0]['name'], 'Appetizers')

    def test_menu_view(self):
        # Test the Menu API endpoint
        response = self.client.get('/api/menus/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the menu items are in the response data
        menu_items = response.json()
        self.assertEqual(len(menu_items), 2)
        
        # Check if the first menu item is 'Spring Rolls'
        self.assertEqual(menu_items[0]['name'], 'Spring Rolls')
        self.assertEqual(menu_items[0]['price'], 5.99)
        self.assertEqual(menu_items[0]['description'], 'Crispy spring rolls with dipping sauce.')
        self.assertEqual(menu_items[0]['category'], 'Appetizers')

        # Check if the second menu item is 'Garlic Bread'
        self.assertEqual(menu_items[1]['name'], 'Garlic Bread')
        self.assertEqual(menu_items[1]['price'], 3.99)
        self.assertEqual(menu_items[1]['description'], 'Warm garlic bread with butter.')
        self.assertEqual(menu_items[1]['category'], 'Appetizers')




