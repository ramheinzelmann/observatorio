

def noticias_home(noticias):

    try:
        dict_noticias = []
        for noticia in noticias:
            if noticia["publicar"] == 1:
                publicar = {
                    "id": noticia["id"],
                    "titulo": noticia["titulo"],
                    "data": noticia["data"],
                    "publicar": noticia["publicar"],
                    "fonte": noticia["fonte"],
                    "imagem": noticia["imagem"],
                    "resumo": noticia["resumo"],
                    "url": noticia["url"],
                }
                dict_noticias.append(publicar)

        noticia01 = dict_noticias[0]
        noticia02 = dict_noticias[1]

        return noticia01, noticia02

    except Exception as e:
        noticia01 = None
        noticia02 = None
        return noticia01, noticia02


def pluviograma_home(pluviogramas):

    try:
        dict_pluviograma_publicar = []
        for i in pluviogramas:
            if i["publicar"] == 1:
                publicar = {
                    "id": i["id"],
                    "titulo": i["titulo"],
                    "data": i["data"],
                    "publicar": i["publicar"],
                    "autor_id": i["autor_id"],
                    "imagem_mini_post": i["imagem_mini_post"],
                    "fonte": i["fonte"],
                }
                dict_pluviograma_publicar.append(publicar)

        return dict_pluviograma_publicar

    except Exception as e:
        print(e)
        dict_pluviograma_publicar = None
        return dict_pluviograma_publicar


def dashboard_home(dashboards):

    try:
        dict_pluviograma_publicar = []
        for i in dashboards:
            if i["publicar"] == 1:
                publicar = {
                    "id": i["id"],
                    "titulo": i["titulo"],
                    "data": i["data"],
                    "publicar": i["publicar"],
                    "autor_id": i["autor_id"],
                    "imagem_post": i["imagem_post"],
                    "fonte": i["fonte"],
                }
                dict_pluviograma_publicar.append(publicar)

        return dict_pluviograma_publicar

    except Exception as e:
        print(e)
        dict_pluviograma_publicar = None
        return dict_pluviograma_publicar
