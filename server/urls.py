"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView
# from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menus/', include('menus.urls')),
    path('api/', include('profiles.urls')),
    path('api/contact/', include('contact.urls')),  # Include the contact app URLs
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
    # path('redoc/', TemplateView.as_view(
    #     template_name='redoc.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='redoc'),
    # path('openapi/', get_schema_view(
    #     title="Restaurant API",
    #     description="API untuk Website Restaurant Keluarga Solo",
    #     version="1.0.0"
    # ), name='openapi-schema'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)