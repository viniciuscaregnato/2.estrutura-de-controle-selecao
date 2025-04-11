"""
Programa: Estrutura de controle seleção. exercicio 1
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
if numero < 10:
    numero = 2*numero
    print(numero)
else:
    frase = "numero nao é valido"
    print(frase)
