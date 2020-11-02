

def noticias_home(noticias):

    try:
        dict_noticias = []
        for noticia in noticias:
            if noticia["publicar"] == 1:
                noticias = {
                    "id": noticia["id"],
                    "titulo": noticia["titulo"],
                    "data": noticia["data"],
                    "publicar": noticia["publicar"],
                    "fonte": noticia["fonte"],
                    "imagem": noticia["imagem"],
                    "resumo": noticia["resumo"],
                    "url": noticia["url"],
                }
                dict_noticias.append(noticias)

        noticia01 = dict_noticias[0]
        noticia02 = dict_noticias[1]

        return noticia01, noticia02

    except Exception as e:
        noticia01 = None
        noticia02 = None
        return noticia01, noticia02


def pluviograma_home(pluviograma):

    try:
        dict_pluviograma = []
        for i in pluviograma:
            if i["publicar"] == 1:
                noticias = {
                    "id": i["id"],
                    "titulo": i["titulo"],
                    "resumo": i["resumo"],
                    "imagem": i["imagem"],
                    "data": i["data"],
                    "publicar": i["publicar"],
                    "autor_id": i["autor_id"],
                }
                dict_pluviograma.append(noticias)

        pluviograma01 = dict_pluviograma[0]
        pluviograma02 = dict_pluviograma[1]

        return pluviograma01, pluviograma02

    except Exception as e:
        print(e)
        pluviograma01 = None
        pluviograma02 = None
        return pluviograma01, pluviograma02