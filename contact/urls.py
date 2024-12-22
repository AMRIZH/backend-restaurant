from django.urls import path
from .views import ContactCreateAPIView, TestimonialListCreateView

urlpatterns = [
    path('', ContactCreateAPIView.as_view(), name='contact-create'),
    path('testimonials/', TestimonialListCreateView.as_view(), name='testimonial-list-create')
]
