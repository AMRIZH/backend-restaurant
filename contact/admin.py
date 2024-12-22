from django.contrib import admin
from .models import Contact, Testimonial

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'text', 'id')
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'email', 'phone_number')  # Display fields in admin
    search_fields = ('name', 'email', 'phone_number')           # Enable search
    list_filter = ('rating',)                                   # Filter by rating