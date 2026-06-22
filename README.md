# App de Leitura 📚

Um sistema simples e robusto para gerenciamento e acompanhamento do progresso de leitura de livros, desenvolvido em Python aplicando os conceitos de **Programação Orientada a Objetos (POO)** e **Testes Automatizados**.

---

## 🚀 Últimas Atualizações

Nesta última versão, o projeto passou por uma grande refatoração para seguir as melhores práticas do mercado (padrões de arquitetura e Clean Code):

* **Separação de Conceitos (Abstração):** As classes foram totalmente isoladas de interações com o usuário (`inputs`). Agora, a classe `Livro` cuida exclusivamente do estado do livro, e a classe `Biblioteca` gerencia a estante virtual.
* **Prevenção de Bugs:** Adicionado tratamento para divisão por zero no cálculo de progresso e validação de páginas (bloqueando páginas negativas ou acima do total do livro).
* **Testes Automatizados:** Implementação de uma suíte de testes unitários utilizando o módulo `unittest` do Python para garantir que as regras de negócio funcionem perfeitamente em menos de 0.002 segundos.

---

## 🛠️ Estrutura do Projeto

* `biblioteca.py`: Contém as classes de negócio `Livro` e `Biblioteca`.
* `testeclasses.py`: Arquivo responsável por rodar os testes automatizados de todas as funções.

---

## 🧪 Como Rodar os Testes Automatizados

Para garantir que o sistema está funcionando perfeitamente e sem erros após a atualização, execute o comando abaixo no seu terminal:

```bash
python testeclasses.py
