from django.shortcuts import render
from .api import get
# Create your views here.

def advice(request):
    call = get()

    advices = {
        "call": call,
    }
    
    return render(request, 'home.html', advices)