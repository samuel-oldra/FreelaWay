from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('Cadastro')

def logar(request):
    return  HttpResponse('Logar')
