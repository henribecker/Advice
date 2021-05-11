from django.shortcuts import render
from . import api

# Create your views here.

def advice(request):
    call = api.get()
    if call == False:
        advices = {
            "call": "SORRY! Indisponível no momento.",
        }
        
        return render(request, 'home.html', advices)
    else:
        advices = {
            "call": call,
        }
        
        return render(request, 'home.html', advices)


def dolar(request):

    cot = api.dolarget()
    preco = float(cot[0])

    context = {
        "dolarhoje" : cot[0][:4],
        "high": cot[1],
        "low": cot[2],
    }

    return render(request, 'dola.html', context)