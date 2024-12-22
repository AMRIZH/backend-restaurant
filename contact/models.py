from django.db import models
from PIL import Image
import uuid

def generate_unique_filename(instance, filename):
    # Generate a unique UUID and append it to the original file extension
    extension = filename.split('.')[-1]
    return f'testimonials/{uuid.uuid4()}.{extension}'

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)  # Optional
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Optional
    rating = models.PositiveSmallIntegerField()  # 1-5 stars
    text = models.TextField()
    image = models.ImageField(upload_to=generate_unique_filename, null=True, blank=True)  # Custom function for unique names

    def __str__(self):
        return f"{self.name} ({self.rating} stars)"

    def save(self, *args, **kwargs):
        # Check if an image is provided and resize it
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')  # Ensure the image is in RGB mode
            img = img.resize((64, 64), Image.ANTIALIAS)  # Resize image to 64x64 pixels

            # Save the resized image back to the same location
            from io import BytesIO
            import os

            # Create a BytesIO buffer to store the image data
            img_io = BytesIO()
            img.save(img_io, 'JPEG', quality=90)  # Save as JPEG with reduced quality (optional)
            img_io.seek(0)

            # Save the image to the model field
            self.image.save(os.path.basename(self.image.name), img_io, save=False)

        super().save(*args, **kwargs)  # Call the parent class save method
