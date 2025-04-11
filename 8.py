"""
Programa: Estrutura de controle seleção. exercicio 8
Descrição:  solicite as notas de um aluno nas avalia¸c˜oes previstas no plano de ensino desta disciplina,
calcule a sua m´edia e informe se o aluno esta aprovado ou reprovado com base nas notas
obtidas, incluindo a recupera¸c˜ao. Use este programa para avaliar seu proprio desempenho
na disciplina.

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 10/04/2025
"""

# Armazenamento de dados
teste1 = 0
teste2 = 0
prova = 0
nota_final = 0

# Entrada de dados
teste1 = float(input("Qual a sua nota no teste 1? "))
teste2 = float(input("Qual a sua nota no teste 2? "))
prova = float(input("Qual a sua nota na prova? "))

# Processamento
nota_final = teste1*0.15 + teste2*0.15 + prova*0.7

# Saída de dados
print(nota_final)

