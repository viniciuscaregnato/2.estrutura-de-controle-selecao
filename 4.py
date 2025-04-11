"""
Programa: Estrutura de controle seleção. exercicio 4
Descrição: leia o nome e a idade de uma pessoa. Se a pessoa tiver menos de 18 anos, imprimir
”[nome] nao pode assistir a este filme.” onde no lugar de [nome] deve sair o nome lido do
teclado.

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 10/04/2025
"""

# Armazenamento de dados
idade = 0
nome = ""

# Entrada de dados
nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))

# Processamento e saída de dados
if idade < 18:
    frase = f"{nome} nao pode assistir a este filme."
    print(frase)

