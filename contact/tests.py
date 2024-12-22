# contact/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Contact, Testimonial
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            text="Test message"
        )

    def test_contact_model_creation(self):
        """Test the creation of a Contact object."""
        self.assertEqual(self.contact.name, "John Doe")
        self.assertEqual(self.contact.email, "john@example.com")
        self.assertEqual(self.contact.phone_number, "1234567890")
        self.assertEqual(self.contact.text, "Test message")
        self.assertEqual(str(self.contact), "John Doe")

class TestimonialModelTest(TestCase):
    def setUp(self):
        self.testimonial = Testimonial.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            phone_number="0987654321",
            rating=5,
            text="Excellent service",
            image=self.create_test_image()
        )

    def create_test_image(self):
        """Helper method to create a test image."""
        image = Image.new('RGB', (100, 100), color='red')
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        return SimpleUploadedFile("test_image.jpg", image_io.read(), content_type="image/jpeg")

    def test_testimonial_model_creation(self):
        """Test the creation of a Testimonial object."""
        self.assertEqual(self.testimonial.name, "Jane Doe")
        self.assertEqual(self.testimonial.email, "jane@example.com")
        self.assertEqual(self.testimonial.phone_number, "0987654321")
        self.assertEqual(self.testimonial.rating, 5)
        self.assertEqual(self.testimonial.text, "Excellent service")
        self.assertTrue(self.testimonial.image.name.startswith("testimonials/"))
        self.assertEqual(str(self.testimonial), "Jane Doe (5 stars)")


class ContactSerializerTest(TestCase):
    def setUp(self):
        self.contact_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone_number": "1234567890",
            "text": "Test message"
        }
        self.client = APIClient()

    def test_contact_serializer_valid(self):
        """Test the Contact serializer with valid data."""
        response = self.client.post('/api/contact/', self.contact_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.contact_data['name'])
        self.assertEqual(response.data['email'], self.contact_data['email'])

    def test_contact_serializer_invalid(self):
        """Test the Contact serializer with invalid data."""
        invalid_data = self.contact_data.copy()
        invalid_data['email'] = 'invalid-email'
        response = self.client.post('/api/contact/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TestimonialSerializerTest(TestCase):
    def setUp(self):
        self.testimonial_data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone_number": "0987654321",
            "rating": 5,
            "text": "Excellent service",
            "image": self.create_test_image()
        }
        self.client = APIClient()

    def create_test_image(self):
        """Helper method to create a test image."""
        image = Image.new('RGB', (100, 100), color='blue')
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        return SimpleUploadedFile("test_image.jpg", image_io.read(), content_type="image/jpeg")

class ContactAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.contact_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone_number": "1234567890",
            "text": "Test message"
        }

    def test_create_contact(self):
        """Test the ContactCreateAPIView."""
        response = self.client.post('/api/contact/', self.contact_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.contact_data['name'])

class TestimonialAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.testimonial_data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone_number": "0987654321",
            "rating": 5,
            "text": "Excellent service",
            "image": self.create_test_image()
        }

    def create_test_image(self):
        """Helper method to create a test image."""
        image = Image.new('RGB', (100, 100), color='green')
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        return SimpleUploadedFile("test_image.jpg", image_io.read(), content_type="image/jpeg")

    def test_list_testimonials(self):
        """Test listing testimonials."""
        response = self.client.get('/api/contact/testimonials/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

