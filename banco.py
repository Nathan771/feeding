from validacoes import validate_user
import time


banco = []

def create_user():
    while True:
        novo_id= input("Insira o id desse usuário: ")
        novo_nome = input("Insira o nome de usuário: ")
        if validate_user(novo_nome, banco)
            banco.append({f"id: ": {id}, "nome: ": {nome}})
            time.sleep(2)
            print("Adicionado com sucesso! ")
        else:
            print("Usuário já existente! ")

        print(banco)



create_user()
