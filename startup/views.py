from django.shortcuts import render
from django.http import Http404

def index(request):
    context = {
        "first": 'Welcome to my advice'
    }

    return render(request, 'base.html', context)

