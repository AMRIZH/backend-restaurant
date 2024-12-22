from rest_framework import serializers
from .models import Contact, Testimonial

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone_number', 'text']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'email', 'phone_number', 'rating', 'text', 'image']
        extra_kwargs = {
            'rating': {'min_value': 1, 'max_value': 5},  # Restrict rating between 1 and 5
        }
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value