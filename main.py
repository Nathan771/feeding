import psycopg2
from validacoes import validate_user
from database import get_connection, create_table

create_table()

def create_user():
    while True:
        novo_id= input("Insira o id desse usuário: ")
        novo_nome = input("Insira o nome de usuário: ")

        if validate_user(novo_nome):
            try:
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("INSERT INTO usuarios (user_id_input, nome) VALUES (%s, %s)", (novo_id, novo_nome))
                conn.commit()
                cur.close()
                conn.close()
                print("Salvo com sucesso! ")

            except psycopg2.errors.UniqueViolation:
                conn.rollback()
                print("Usuário já existe! ")
            
            finally:
                cur.close()
                conn.close()


create_user()
