from .views import about_us, contact_us
from django.urls import path
urlpatterns = [
    path('about', about_us, name='about'),
    path('contact', contact_us, name='contact'),
]
