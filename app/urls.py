from django.urls import path, include
from . import views, models


urlpatterns = [
    path('', views.index, name='index'),
    path('noticias', views.noticias, name='noticias'),
    path('temperatura', views.temperatura, name='temperatura'),
    path('precipitacao', views.precipitacao, name='precipitacao'),
    path('publicacoes', views.publicacoes, name='publicacoes'),
]
