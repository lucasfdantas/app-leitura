livros = []

# Função para adicionar livros
'''

Após ser invocada, adiciona os campos de titulo, autor, número de páginas e número atual de páginas.
Para isso utiliza o append e adiciona ao final da lista o dicionario contendo as chaves e valores dos campos mencionados.

'''
def adicionar_livro(titulo, autor, paginas, pag_atual):
    livros.append({'titulo': titulo, 'autor': autor, 'paginas': paginas, 'pag_atual': pag_atual})
    print('Livro adicionado à biblioteca com sucesso!')

# Função para atualizar livro

'''

Após ser invocada a função realiza atualização do número atual de páginas fazendo a verificação. Para não ter o número de páginas acima do registro inicial.

'''

def atualizar_livro(livro, pag_atual):
    if pag_atual < 0 or pag_atual > livro['paginas']:
        print("Número de página inválido para este livro.")
        return False
    livro['pag_atual'] = pag_atual
    print('Número atual de páginas updated com sucesso!')
    return True

# Função excluir livro

'''

Função para deletar o livro na lista livros, ela ao final faz uma verificação validando se a variavel 'removido' foi atribuido o valor 'True', 
se caso não for imprime a informção que não existe

'''

def excluir_livro(remover):
    removido = False
    for i, livro in enumerate(livros):
        if livro['titulo'].lower() == remover.lower():
            livros.pop(i)
            removido = True
            break
    print('Livro removido com sucesso!' if removido else 'Não existe esse título.')

# Listar livros em formato de tabela estruturada
'''

Função quando invocada, imprime a tabela com as colunas titulo, autor e número de páginas e total de páginas

'''


def listar_livros_tabela():
    if not livros:
        print('A biblioteca está vazia.')
        return

    print('\n' + '=' * 90)
    # Cabeçalho da tabela com espaçamentos definidos (<30 significa alinhado à esquerda com 30 espaços)
    print(f"{'NOME DO LIVRO':<30} | {'AUTOR':<25} | {'PÁG. LIDAS':<12} | {'PÁG. RESTANTES':<14}")
    print('-' * 90)

    for livro in livros:
        titulo = livro['titulo']
        autor = livro['autor']
        lidas = livro['pag_atual']
        # Cálculo das páginas restantes (garantindo que não seja negativo)
        restantes = max(0, livro['paginas'] - lidas)

        # Se o título ou autor forem muito longos, eles são cortados para não quebrar a tabela
        titulo_formatado = titulo[:27] + '...' if len(titulo) > 30 else titulo
        autor_formatado = autor[:22] + '...' if len(autor) > 25 else autor

        print(f"{titulo_formatado:<30} | {autor_formatado:<25} | {lidas:<12} | {restantes:<14}")
    
    print('=' * 90 + '\n')

# Função progresso_total
'''

Função calcula o número de páginas lidas até o momento imprimindo o históriocos.

'''

def progresso_total():
    total_livros = len(livros)
    livros_lidos = 0
    paginas_totais_lidas = 0
    for livro in livros:
        atual = livro['pag_atual']
        total = livro['paginas']
        paginas_totais_lidas += atual
        if atual >= total:
            livros_lidos += 1
            
    print('\n=== Estatísticas Gerais ===')
    print(f'Total de livros no histórico: {total_livros}')
    print(f'Livros concluídos: {livros_lidos}')
    print(f'Total de páginas lidas: {paginas_totais_lidas}')
    print('===========================\n')

# Função progresso unitario
def progresso_unitario(livro_atual):
    encontrado = False
    for livro in livros:
        if livro['titulo'].lower() == livro_atual.lower():
            total = livro['paginas']
            atual = livro['pag_atual']
            porcentagem_lida = (atual / total) * 100
            
            print(f'\nLivro: {livro["titulo"]}')
            print(f'Progresso atual: {atual}/{total} páginas lidas.')
            print(f'Você já leu {porcentagem_lida:.1f}% desse livro.')
            
            if atual >= total:
                print('Parabéns! Você concluiu este livro! 🏆')
                
            encontrado = True
            break
            
    if not encontrado:
        print('Livro não encontrado!')

# Função do sub-menu
def menu_vp():
    if not livros:
        print('Você não tem livros adicionados.')
        return
    while True:
        print('''\n=== PROGRESSO DE LEITURA ===
1 - Ver progresso atual da biblioteca
2 - Ver progresso de um título específico
3 - Voltar ao menu principal
''')
        opcao_vp = input('Escolha uma opção: ')
        match opcao_vp:
            case '1':
                progresso_total()
            case '2':
                livro_atual = input('Digite o título para checar o progresso: ').strip()
                progresso_unitario(livro_atual)          
            case '3':
                print('Voltando para o menu principal...')
                break
            case _: 
                print('Opção inválida')

# Função principal
def main():
    print('''Bem-vindo ao My Progress Reading
Veja seu progresso na leitura no ano!''')
    while True:
        print('''\nDigite a opção desejada:
1 - Adicionar livro
2 - Atualizar histórico de leitura
3 - Excluir livro do histórico
4 - Verificar progresso de leitura
5 - Listar todos os livros (Tabela)
6 - Sair''')    
        opcao = input('Digite a opção: ')
        match opcao:
            case '1':
                try:
                    titulo = input("Qual título do livro? ").strip()
                    autor = input("Qual o nome do autor? ").strip()
                    paginas = int(input("Quantas páginas tem o livro? "))
                    pag_atual = int(input("Em qual página você está atualmente? "))
                    
                    if paginas <= 0:
                        print("O livro precisa ter pelo menos 1 página!")
                    else:
                        adicionar_livro(titulo, autor, paginas, pag_atual)
                except ValueError:
                    print('Erro: Por favor, digite números válidos para as páginas.')

            case '2':
                titulo_busca = input('Qual título deseja atualizar? ').strip()
                livro_encontrado = None
                
                for livro in livros:
                    if livro['titulo'].lower() == titulo_busca.lower():
                        livro_encontrado = livro
                        break
                
                if livro_encontrado:
                    try:
                        pag_atual = int(input(f"Qual a página atual? (Total: {livro_encontrado['paginas']}): "))
                        atualizar_livro(livro_encontrado, pag_atual)
                    except ValueError:
                        print('Erro: Digite um número inteiro válido.')
                else:
                    print('Título inválido ou não encontrado.')

            case '3':
                remover = input('Qual título deseja remover? ').strip()
                excluir_livro(remover)

            case '4':
                menu_vp()

            case '5':
                listar_livros_tabela()

            case '6':
                print('Saindo do sistema. Boas leituras!')
                break
                
            case _:
                print('Opção inválida')

if __name__ == "__main__":
    main()