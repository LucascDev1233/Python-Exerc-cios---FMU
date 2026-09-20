"""
Exercício 1: Estruturas Condicionais e Operações Matemáticas

Receba um número inteiro positivo.
- Se for par, calcule seu quadrado.
- Se for ímpar, calcule seu cubo.
"""

num = int(input("Digite um número inteiro positivo: "))

if num <= 0:
    print("Erro: digite um número positivo.")

elif num % 2 == 0:
    quadrado = num ** 2
    print(f"O quadrado de {num} é: {quadrado}")

else:
    cubo = num ** 3
    print(f"O cubo de {num} é: {cubo}")