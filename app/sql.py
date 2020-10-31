import sqlite3


def conexao_db():
    conn = sqlite3.connect('db.observatorio')
    cursor = conn.cursor()

    return [conn, cursor]


def get_noticias():
    conn, cursor = conexao_db()
    cursor.execute(f"""SELECT * FROM app_noticias;""")

    noticias = None

    list_noticias = []
    for linha in cursor.fetchall():
        noticias = {
            "id": linha[0],
            "titulo": linha[1],
            "url": linha[2],
            "fonte": linha[3],
            "resumo": linha[4],
            "imagem": linha[5],
            "data": linha[6],
            "autor_id": linha[7],
            "publicar": linha[8],
        }

        list_noticias.append(noticias)

    conn.close()

    if not list_noticias:
        return list_noticias

    return list_noticias


def get_pluviograma():
    conn, cursor = conexao_db()
    cursor.execute(f"""SELECT * FROM app_pluviograma;""")

    pluviograma = None

    list_pluviograma = []
    for linha in cursor.fetchall():
        pluviograma = {
            "id": linha[0],
            "titulo": linha[1],
            "resumo": linha[2],
            "imagem": linha[3],
            "data": linha[4],
            "publicar": linha[5],
            "autor_id": linha[6],
        }

        list_pluviograma.append(pluviograma)

    conn.close()

    if not list_pluviograma:
        return list_pluviograma

    return list_pluviograma
