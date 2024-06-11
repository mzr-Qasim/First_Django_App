
from django.urls import path
from .views import homePage

urlpatterns = [
    # Other URL patterns
    path('home/', homePage, name='Home'),
]