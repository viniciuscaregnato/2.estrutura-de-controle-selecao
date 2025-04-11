"""
Programa: Estrutura de controle seleção. exercicio 6
Descrição: leia um texto e informe se ele ´e o nome da capital de um estado da regiao sul do Brasil.

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 10/04/2025
"""

# Armazenamento de dados
capital = ""
lista_capitais = []

# Entrada de dados
capital = input("Digite uma capital da regiao sul do Brasil: ")
lista_capitais = ["Porto Alegre", "Curitiba", "Florianópolis"]

# Processamento e saída de dados
if capital in  lista_capitais:
    frase = "É uma capital da regiao sul do brasil"
else:
    frase = "Nao é uma capital da regiao sul do brasil"

# Saída de dados
print(frase)