from django.urls import path
from .views import sandwich_steps, sandwich_ingredients

urlpatterns = [
    path('api/sandwich-steps/', sandwich_steps, name='sandwich_steps'),
    path('api/sandwich-ingredients/', sandwich_ingredients, name='sandwich_ingredients'),
]
