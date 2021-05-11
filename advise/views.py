from django.shortcuts import render
from .api import get

# Create your views here.

def advice(request):
    call = get()

    advices = {
        "call": call,
    }
    
    return render(request, 'home.html', advices)


def dolar(request):

    cot = dolarget()

    context = {
        "dolarhoje" : cot[0],
        "high": cot[1],
        "low": cot[2],
    }

    return render(request, 'dola.html', context)