from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='Home'),
    path('advice/', advice, name='Advice'),
]