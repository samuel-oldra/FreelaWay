from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        print(f'{username} | {senha} | {confirmar_senha}')
        return HttpResponse('Recebido')


def logar(request):
    return HttpResponse('Logar')
