class Biblioteca:
    ''' Esta classe representa uma biblioteca que pode armazenar livros, listar os livros disponíveis, retirar livros pelo título e calcular o progresso total de leitura.'''
    def __init__(self):
        self.biblioteca = []

    def AddLivro(self, livro):
        self.biblioteca.append(livro)

    def ListarLivros(self): # Removido o parâmetro 'livros'
           
        # Agora usamos 'self.biblioteca' interna da classe
        if not self.biblioteca:
            print('A biblioteca está vazia.')
            return
        
        print('\n' + '=' * 90)
        print(f"{'NOME DO LIVRO':<30} | {'AUTOR':<25} | {'PÁG. LIDAS':<12} | {'PÁG. RESTANTES':<14}")
        print('-' * 90)
    
        # Varre a lista interna de livros
        for livro in self.biblioteca:
            # Acessando como OBJETOS (livro.atributo)
            titulo = livro.titulo
            autor = livro.autor
            lidas = livro.pagina_atual
            
            # Cálculo usando o atributo total de páginas do objeto livro
            restantes = max(0, livro.paginas - lidas)
    
            titulo_formatado = titulo[:27] + '...' if len(titulo) > 30 else titulo
            autor_formatado = autor[:22] + '...' if len(autor) > 25 else autor
    
            print(f"{titulo_formatado:<30} | {autor_formatado:<25} | {lidas:<12} | {restantes:<14}")
        
        print('=' * 90 + '\n')
    
    def RetirarLivro(self, remover):
        removido = False
        for i, livro in enumerate(self.biblioteca):
            if livro.titulo.lower() == remover.lower():
                self.biblioteca.pop(i)
                removido = True
                break
        print('Livro removido com sucesso!' if removido else 'Não existe esse título.')
    
    def ProgressoTotal(self):
        total_livros = len(self.biblioteca)
        livros_lidos = 0
        paginas_totais_lidas = 0
        for livro in self.biblioteca:
            atual = livro.pagina_atual
            total = livro.paginas
            paginas_totais_lidas += atual
            if atual >= total:
                livros_lidos += 1
                    
        print('\n=== Estatísticas Gerais ===')
        print(f'Total de livros no histórico: {total_livros}')
        print(f'Livros concluídos: {livros_lidos}')
        print(f'Total de páginas lidas: {paginas_totais_lidas}')
        print('===========================\n')
        


class Livro:
    
    ''' Esta classe representa um livro com título, autor, número total de páginas e a página atual que o leitor está. Ela possui métodos para atualizar a página atual e calcular o progresso de leitura.'''
    
    def __init__(self, titulo, autor, paginas, pagina_atual=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_atual = pagina_atual
    def AtualizarPagina(self, nova_pagina):
        if 0 <= nova_pagina <= self.paginas:
            self.pagina_atual = nova_pagina
            print(f'Página atualizada para {nova_pagina} no livro "{self.titulo}".')
        else:
            print(f'Número de página inválido. O livro "{self.titulo}" tem {self.paginas} páginas.')
    def ProgressoUnitario(self):     
        progresso = (self.pagina_atual / self.paginas) * 100 if self.paginas > 0 else 0
        print(f'Progresso do livro "{self.titulo}": {progresso:.2f}%')
        
