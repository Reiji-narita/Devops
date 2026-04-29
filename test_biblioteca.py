import unittest
from biblioteca import Biblioteca

class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.b = Biblioteca()

    def test_adicionar_livro(self):
        self.b.adicionar_livro("Python", "Reiji")
        self.assertEqual(len(self.b.livros), 1)

    def test_listar_livros(self):
        self.b.adicionar_livro("Python", "Reiji")
        livros = self.b.listar_livros()
        self.assertEqual(len(livros), 1)

    def test_emprestar_livro(self):
        self.b.adicionar_livro("Python", "Reiji")
        resultado = self.b.emprestar_livro("Python")
        self.assertTrue(resultado)

    def test_emprestar_livro_ja_emprestado(self):
        self.b.adicionar_livro("Python", "Reiji")
        self.b.emprestar_livro("Python")
        resultado = self.b.emprestar_livro("Python")
        self.assertFalse(resultado)

    def test_devolver_livro(self):
        self.b.adicionar_livro("Python", "Reiji")
        self.b.emprestar_livro("Python")
        resultado = self.b.devolver_livro("Python")
        self.assertTrue(resultado)

    def test_devolver_livro_nao_emprestado(self):
        self.b.adicionar_livro("Python", "Reiji")
        resultado = self.b.devolver_livro("Python")
        self.assertFalse(resultado)

    def test_buscar_livro(self):
        self.b.adicionar_livro("Python", "Reiji")
        livro = self.b.buscar_livro("Python")
        self.assertIsNotNone(livro)

    def test_buscar_livro_inexistente(self):
        livro = self.b.buscar_livro("Java")
        self.assertIsNone(livro)


if __name__ == "__main__":
    unittest.main()