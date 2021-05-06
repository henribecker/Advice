from django.shortcuts import render
from .api import get
# Create your views here.

def home(request):
    
    context = {
        "call": 'Welcome',
    }

    return render(request, 'home.html', context)

def advice(request):
    call = get()

    advices = {
        "call": call,
    }
    
    return render(request, 'home.html', advices)