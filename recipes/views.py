from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Pedro Lisboa'
    })


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')
