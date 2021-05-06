from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect



def index(request):

    context = {
        "first": 'Welcome to my advice'
    }

    return render(request, 'base.html', context)
