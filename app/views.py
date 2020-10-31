
from django.shortcuts import render

from app.app import noticias_home, pluviograma_home
from app.sql import get_noticias, get_pluviograma
from app.models import Noticias, Tempertura, Precipitacao, Teams, Publicacoes, Pluviograma


def index(request):

    noticias = get_noticias()
    pluviograma = get_pluviograma()

    if not noticias or not pluviograma:
        return render(request, 'index.html')

    noticia01, noticia02 = noticias_home(noticias)

    pluviograma01, pluviograma02 = pluviograma_home(pluviograma)

    teams = Teams.objects.all()

    return render(request, 'index.html', {'noticia01': noticia01, 'noticia02': noticia02, 'teams': teams,
                                          'pluviograma01': pluviograma01, 'pluviograma02': pluviograma02})


def noticias(request):

    noticias = Noticias.objects.all()
    if not noticias:
        return render(request, 'app/noticias.html')

    return render(request, 'app/noticias.html', {'dados': noticias})


def temperatura(request):

    temperatura = Tempertura.objects.all()
    if not temperatura:
        return render(request, 'app/temperatura.html')

    return render(request, 'app/temperatura.html', {'dados': temperatura})


def precipitacao(request):

    precipitacao = Precipitacao.objects.all()
    if not precipitacao:
        return render(request, 'app/precipitacao.html')

    return render(request, 'app/precipitacao.html', {'dados': precipitacao})


def publicacoes(request):

    publicacoes = Publicacoes.objects.all()
    if not noticias:
        return render(request, 'app/publicacoes.html')

    return render(request, 'app/publicacoes.html', {'dados': publicacoes})
