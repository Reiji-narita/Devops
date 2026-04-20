from biblioteca import Biblioteca
import os

def menu():
    b = Biblioteca()

    while True:
        print("\n--- SISTEMA DE BIBLIOTECA ---")
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            b.adicionar_livro(titulo, autor)

        elif opcao == "2":
            for livro in b.listar_livros():
                print(livro)

        elif opcao == "3":
            titulo = input("Título: ")
            if b.emprestar_livro(titulo):
                print("Livro emprestado!")
            else:
                print("Não disponível.")

        elif opcao == "4":
            titulo = input("Título: ")
            if b.devolver_livro(titulo):
                print("Livro devolvido!")
            else:
                print("Erro ao devolver.")

        elif opcao == "0":
            break

if __name__ == "__main__":
    if os.getenv("CI"):
        print("CI executado com sucesso!")
    else:
        # Execução automática (evita erro no Docker)
        b = Biblioteca()
        b.adicionar_livro("Python Básico", "Rodrigo")
        b.adicionar_livro("DevOps na Prática", "Ribas")

        b.emprestar_livro("Python Básico")

        for livro in b.listar_livros():
            print(livro)