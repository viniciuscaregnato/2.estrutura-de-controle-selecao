"""
Programa: Estrutura de controle seleção. exercicio 9
Descrição: leia o peso e a altura de uma pessoa, calcule seu´ındice de massa corporal (IMC), classifique
essa pessoa de acordo com a tabela abaixo e escreva na tela a condi¸c˜ao da pessoa:

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 10/04/2025
"""

# Armazenamento de dados
peso = 0
altura = 0
IMC = 0

# Entrada de dados
peso = float(input("Qual seu peso (kg)? "))
altura = float(input("Qual a sua altura (m)? "))

# Processamento
IMC = peso/altura**2

if IMC <= 18.5:
    frase = "Excessivamente magro"
elif IMC < 25:
    frase = "peso normal"
elif IMC < 30:
    frase = "sobrepeso"
else:
    frase = "obeso"

# Saída de dados

print(frase)