from django.contrib import admin
from app.models import Noticias, Tempertura, Precipitacao, Teams, Publicacoes, Queimadas, Alagamento, \
    Reservatorios, Projetos, Pluviograma, Dashboard, Imagens_Banner, Post

# Register your models here.

admin.site.register(Noticias)
admin.site.register(Tempertura)
admin.site.register(Precipitacao)
admin.site.register(Teams)
admin.site.register(Publicacoes)
admin.site.register(Queimadas)
admin.site.register(Alagamento)
admin.site.register(Reservatorios)
admin.site.register(Projetos)
admin.site.register(Pluviograma)
admin.site.register(Dashboard)
admin.site.register(Imagens_Banner)
admin.site.register(Post)
