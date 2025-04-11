"""
Programa: Estrutura de controle seleção. exercicio 3
Descrição: leia um numero, determine se ele é multiplo de 3 e imprima na tela a mensagem "Este numero é multiplo de 3” ou ”Este numero nao é multiplo de 3” a depender do caso.

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/04/2025
"""

# Armazenamento de dados
numero = 0
frase = ""

# Entrada de dados
numero = float(input("Digite um numero: "))

# Processamento de dados
if numero % 3 == 0:
    frase = "numero multiplo de tres"
else:
    frase = "numerao nao é multiplo de 3"

# Saída de dados
print(frase)