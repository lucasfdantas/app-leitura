import unittest
''' Este arquivo contém testes automatizados para as classes Biblioteca e Livro.
Utilizamos a biblioteca unittest do Python para criar casos de teste que validam o comportamento esperado das funcionalidades implementadas.
Cada método de teste começa com "test_" e verifica uma funcionalidade específica, como adicionar um livro, remover um livro, ou atualizar a página atual de um livro. O método setUp é utilizado para criar um cenário limpo antes de cada teste, garantindo que os testes sejam independentes entre si.
TESTE CRIADO COM AJUDA DE IA (GEMINI) PARA VALIDAR O FUNCIONAMENTO DAS CLASSES E MÉTODOS IMPLEMENTADOS.
'''

from biblioteca import Biblioteca, Livro 


class TestSistemaBiblioteca(unittest.TestCase):

    def setUp(self):
        """O método setUp roda ANTES de cada teste. 
        Ideal para criar um cenário limpo."""
        self.estante = Biblioteca()
        self.livro_teste = Livro("O Hobbit", "Tolkien", 300)

    # --- TESTES DA CLASSE BIBLIOTECA ---

    def test_adicionar_livro_na_biblioteca(self):
        # Executa a ação
        self.estante.AddLivro(self.livro_teste)
        
        # Valida se a quantidade de livros na biblioteca agora é 1
        self.assertEqual(len(self.estante.biblioteca), 1)
        # Valida se o livro que está lá dentro é o mesmo que adicionamos
        self.assertEqual(self.estante.biblioteca[0].titulo, "O Hobbit")

    def test_remover_livro_com_sucesso(self):
        # Cenário: biblioteca começa com um livro
        self.estante.AddLivro(self.livro_teste)
        
        # Executa a remoção pelo título
        self.estante.RetirarLivro("O Hobbit")
        
        # Valida se a biblioteca ficou vazia
        self.assertEqual(len(self.estante.biblioteca), 0)

    def test_remover_livro_inexistente(self):
        self.estante.AddLivro(self.livro_teste)
        
        # Tenta remover um livro que não existe
        self.estante.RetirarLivro("Livro Inexistente")
        
        # Valida que o livro original ainda continua lá (nada foi removido)
        self.assertEqual(len(self.estante.biblioteca), 1)

    # --- TESTES DA CLASSE LIVRO ---

    def test_atualizar_pagina_valida(self):
        # Tentamos atualizar para a página 150 (o livro tem 300)
        self.livro_teste.AtualizarPagina(150)
        
        # Valida se a página atual foi alterada com sucesso
        self.assertEqual(self.livro_teste.pagina_atual, 150)

    def test_atualizar_pagina_acima_do_limite(self):
        # Tenta ir para a página 350 em um livro de 300 páginas
        self.livro_teste.AtualizarPagina(350)
        
        # Valida que a página NÃO foi alterada (deve continuar 0)
        self.assertEqual(self.livro_teste.pagina_atual, 0)

    def test_atualizar_pagina_negativa(self):
        # Tenta ir para uma página inválida negativa
        self.livro_teste.AtualizarPagina(-10)
        
        # Valida que a página continuou 0
        self.assertEqual(self.livro_teste.pagina_atual, 0)


# Executa os testes automatizados
if __name__ == '__main__':
    unittest.main()