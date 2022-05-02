from datetime import datetime
from django.shortcuts import render, redirect

from jobs.models import Jobs


def encontrar_jobs(request):
    if request.method == "GET":
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')

        prazo_minimo = request.GET.get('prazo_minimo')
        prazo_maximo = request.GET.get('prazo_maximo')

        categoria = request.GET.get('categoria')

        if preco_minimo or preco_maximo or prazo_minimo or prazo_maximo or categoria:
            if not preco_minimo:
                preco_minimo = 0
            if not preco_maximo:
                preco_maximo = 999999

            if not prazo_minimo:
                prazo_minimo = datetime(year=1900, month=1, day=1)
            if not prazo_maximo:
                prazo_maximo = datetime(year=3000, month=1, day=1)

            if categoria == '':
                categoria = ['D', 'EV', ]
            elif categoria == 'D':
                categoria = ['D', ]
            elif categoria == "EV":
                categoria = ['EV', ]

            jobs = Jobs.objects \
                .filter(preco__gte=preco_minimo) \
                .filter(preco__lte=preco_maximo) \
                .filter(prazo_entrega__gte=prazo_minimo) \
                .filter(prazo_entrega__lte=prazo_maximo) \
                .filter(categoria__in=categoria) \
                .filter(reservado=False)
        else:
            jobs = Jobs.objects.filter(reservado=False)

        return render(request, 'encontrar_jobs.html', {'jobs': jobs})


def aceitar_job(request, id):
    job = Jobs.objects.get(id=id)
    job.profissional = request.user
    job.reservado = True
    job.save()
    return redirect('/jobs/encontrar_jobs')
