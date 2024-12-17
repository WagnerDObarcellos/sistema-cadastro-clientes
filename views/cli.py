from controllers.auth import register_user, login_user
from models.crud import create_record, read_records, update_record, delete_record
import os

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu principal para autenticação
def menu_autenticacao():
    while True:
        limpar_tela()
        print("=== Sistema CRUD - Autenticação ===")
        print("1. Login")
        print("2. Registrar")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            username = input("Usuário: ")
            password = input("Senha: ")
            if login_user(username, password):
                print("\nLogin bem-sucedido!")
                input("Pressione Enter para continuar...")
                menu_crud()
            else:
                print("\nUsuário ou senha incorretos.")
                input("Pressione Enter para tentar novamente...")
        elif opcao == "2":
            username = input("Escolha um nome de usuário: ")
            password = input("Escolha uma senha: ")
            if register_user(username, password):
                print("\nUsuário registrado com sucesso!")
            else:
                print("\nErro: Usuário já existe.")
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")

# Menu CRUD após o login
def menu_crud():
    while True:
        limpar_tela()
        print("=== Sistema CRUD ===")
        print("1. Criar Registro")
        print("2. Listar Registros")
        print("3. Atualizar Registro")
        print("4. Deletar Registro")
        print("5. Logout")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do registro: ")
            descricao = input("Descrição: ")
            create_record(nome, descricao)
            print("\nRegistro criado com sucesso!")
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            registros = read_records()
            print("\n=== Registros ===")
            for registro in registros:
                print(f"ID: {registro[0]} | Nome: {registro[1]} | Descrição: {registro[2]}")
            input("\nPressione Enter para continuar...")
        elif opcao == "3":
            id_registro = input("ID do registro a ser atualizado: ")
            novo_nome = input("Novo nome: ")
            nova_descricao = input("Nova descrição: ")
            if update_record(id_registro, novo_nome, nova_descricao):
                print("\nRegistro atualizado com sucesso!")
            else:
                print("\nErro: ID não encontrado.")
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            id_registro = input("ID do registro a ser deletado: ")
            if delete_record(id_registro):
                print("\nRegistro deletado com sucesso!")
            else:
                print("\nErro: ID não encontrado.")
            input("Pressione Enter para continuar...")
        elif opcao == "5":
            print("\nFazendo logout...")
            input("Pressione Enter para voltar ao menu de autenticação...")
            break
        else:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")

# Executar o programa
if __name__ == "__main__":
    menu_autenticacao()
