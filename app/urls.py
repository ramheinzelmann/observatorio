from django.urls import path, include
from . import views, models


urlpatterns = [
    path('', views.index, name='index'),
    path('temperatura', views.temperatura, name='temperatura'),
    path('precipitacao', views.precipitacao, name='precipitacao'),
    path('queimada', views.queimada, name='queimada'),
    path('alagamento', views.alagamento, name='alagamento'),
    path('reservatorio', views.reservatorio, name='reservatorio'),
    path('glossario', views.glossario, name='glossario'),
    path('projetos', views.projetos, name='projetos'),
    path('publicacoes', views.publicacoes, name='publicacoes'),
    path('noticias', views.noticias, name='noticias'),
    path('lcgea', views.lcgea, name='lcgea'),
]
