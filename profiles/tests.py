from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import RestaurantProfile, OpeningHour, RestaurantFAQ


class RestaurantProfileTests(TestCase):
    def setUp(self):
        # Create a test RestaurantProfile
        self.profile = RestaurantProfile.objects.create(
            name="Test Restaurant",
            about_us="About Test Restaurant",
            address="Test Address",
            phone="123456789",
            email="test@example.com",
            facebook="https://facebook.com/test",
            instagram="https://instagram.com/test",
            twitter="https://twitter.com/test"
        )
        self.client = APIClient()
        self.url = '/api/profile/'

    def test_get_restaurant_profile(self):
        # Test if RestaurantProfile API is accessible and returns correct data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one profile, as it's a Singleton
        self.assertEqual(response.data[0]['name'], self.profile.name)
        self.assertEqual(response.data[0]['email'], self.profile.email)


class OpeningHourTests(TestCase):
    def setUp(self):
        # Create OpeningHour instances
        self.opening_hour = OpeningHour.objects.create(
            day=0,  # Monday
            opening_time="08:00:00",
            closing_time="22:00:00"
        )
        self.client = APIClient()
        self.url = '/api/opening-hour/'

    def test_get_opening_hours(self):
        # Test if OpeningHours API is accessible and returns correct data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['day'], 'Senin')
        self.assertEqual(response.data[0]['opening_time'], "08:00:00")
        self.assertEqual(response.data[0]['closing_time'], "22:00:00")


class RestaurantFAQTests(TestCase):
    def setUp(self):
        # Create RestaurantFAQ instance
        self.faq = RestaurantFAQ.objects.create(
            question="What are the opening hours?",
            answer="From 8 AM to 10 PM."
        )
        self.client = APIClient()
        self.url = '/api/faq/'

    def test_get_restaurant_faq(self):
        # Test if RestaurantFAQ API is accessible and returns correct data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], self.faq.question)
        self.assertEqual(response.data[0]['answer'], self.faq.answer)
