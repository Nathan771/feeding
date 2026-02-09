from validacoes import validate_user
from database import get_connection, create_table
import time

create_table()

def create_user():
    while True:
        novo_id= input("Insira o id desse usuário: ")
        novo_nome = input("Insira o nome de usuário: ")

        if validate_user(novo_nome):
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO usuarios (user_id_input, nome) VALUES (%s, %s)", (novo_id, novo_nome))
            conn.commit()
            cur.close()

        else:
            print("Usuário já existe! ")
            



create_user()
