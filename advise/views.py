from django.shortcuts import render
from . import api
from .forms import MoedaForm
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


def dolar(request, fisrt, second):

    cot = api.dolarget(fisrt, second)
    if cot == False:
        context = {
        "valor" : cot[0][:4],
        "high": cot[1],
        "low": cot[2],
        }

        return render(request, 'dola.html', context)
    else:
        # preco = float(cot[0])

        context = {
            "valor" : cot[0][:4],
            "high": cot[1],
            "low": cot[2],
        }

        return render(request, 'dola.html', context)


def choice_coin(request):
    context = {}
    context['form'] = MoedaForm()
    if request.GET:
        temp = request.GET['coin_origin']
        temp1 = request.GET['coin_destiny']
        return dolar(request, temp, temp1)


    return render(request, 'choicecoin.html', context)