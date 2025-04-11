"""
Programa: Estrutura de controle seleção. exercicio 2
Descrição: leia um numero e imprima na tela o seu dobro se ele for menor do que 10. Se o numero for de 10 ate 20, imprima a sua metade. Em qualquer outro caso, imprima na tela que o numero nao e valido.

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/04/2025
"""

# Armazenamento de dados
numero = 0
frase = ""

# Entrada de dados
numero = float(input("Digite um numero: "))

# Processamento e saída de dados
if numero % 2 == 0:
    frase = "numero é par"
else:
    frase = "numero é impar"

# Saída de dados
print(frase)