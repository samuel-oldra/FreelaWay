from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
    return render(request, 'cadastro.html')


def logar(request):
    return HttpResponse('Logar')
