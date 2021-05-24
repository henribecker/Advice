from django.shortcuts import render

def index(request):
    context = {
        "first": 'Welcome to my advice'
    }

    return render(request, 'base.html', context)

