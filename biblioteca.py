from models import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))

    def listar_livros(self):
        return self.livros

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def emprestar_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        if livro and not livro.emprestado:
            livro.emprestado = True
            return True
        return False

    def devolver_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        if livro and livro.emprestado:
            livro.emprestado = False
            return True
        return False