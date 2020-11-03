
from django.shortcuts import render

from app.app import noticias_home, pluviograma_home, dashboard_home
from app.sql import get_noticias, get_pluviograma, get_dashboard
from app.models import Noticias, Tempertura, Precipitacao, Teams, Publicacoes, Imagens_Banner


def index(request):

    retorno_pluviograma = get_pluviograma()
    pluviogramas = pluviograma_home(retorno_pluviograma)

    retorno_dashboard = get_dashboard()
    dashboards = dashboard_home(retorno_dashboard)

    noticias = get_noticias()
    noticia01, noticia02 = noticias_home(noticias)

    teams = Teams.objects.all()
    banner = Imagens_Banner.objects.all()

    return render(request, 'index.html', {'noticia01': noticia01, 'noticia02': noticia02, 'teams': teams,
                                          'dashboards': dashboards, 'pluviogramas': pluviogramas,
                                          'banner': banner})


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
