from database import get_connection

def validate_user(nome_digitado):
    conn = get_connection()
    cur = conn.cursor()

    #busca no banco se o nome já existe

    cur.execute("SELECT nome FROM usuarios WHERE nome = LOWER(%s)", (nome_digitado, ))
    usuario = cur.fetchone()

    cur.close()
    conn.close()

    return usuario is None

    