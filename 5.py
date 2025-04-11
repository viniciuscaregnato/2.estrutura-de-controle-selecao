"""
Programa: Estrutura de controle seleção. exercicio 5
Descrição: leia um n´umero e imprima na tela se ele ´e negativo, nulo ou positivo.

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 10/04/2025
"""

# Armazenamento de dados
numero  = 0
frase = ""

# Entrada de dados
numero = int(input("Digite um numero: "))

# Processamento e saída de dados
if numero == 0:
    frase = "seu numero é nulo."
elif numero > 0:
    frase = "seu numero é positivo."
else:
    frase = "seu numero é negativo"

# Saída de dados
print(frase)