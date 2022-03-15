from django.http import HttpResponse
from django.shortcuts import render, redirect


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        print(f'{username} | {senha} | {confirmar_senha}')

        if not senha == confirmar_senha:
            return redirect('/auth/cadastro')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('/auth/cadastro')

        return HttpResponse('Recebido')


def logar(request):
    return HttpResponse('Logar')
