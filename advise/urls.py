from django.urls import path
from .views import *


urlpatterns = [
    path('advice/', advice, name='Advice'),
]