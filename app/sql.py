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
            "fonte": linha[2],
            "resumo": linha[3],
            "imagem": linha[4],
            "data": linha[5],
            "publicar": linha[6],
            "autor_id": linha[7],
            "url": linha[8],
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


def get_dashboard():
    conn, cursor = conexao_db()
    cursor.execute(f"""SELECT * FROM app_dashboard;""")

    dashboards = None

    list_dashboards = []
    for linha in cursor.fetchall():
        dashboards = {
            "id": linha[0],
            "titulo": linha[1],
            "data": linha[2],
            "publicar": linha[3],
            "autor_id": linha[4],
            "imagem_post_01": linha[5],
            "imagem_post_02": linha[6],
            "imagem_post_04": linha[7],
            "imagem_mini_post_01": linha[8],
            "imagem_post_03": linha[9],
        }

        list_dashboards.append(dashboards)

    conn.close()

    if not list_dashboards:
        return list_dashboards

    return list_dashboards
