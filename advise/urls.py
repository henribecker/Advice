from django.urls import path
from .views import *


urlpatterns = [
    path('advice/', advice, name='Advice'),
    path('choice/', choice_coin, name='Choice'),
    path('cotacao/', dolar, name='Dolar'),
]