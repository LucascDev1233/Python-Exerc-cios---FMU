num1 = float(input("Digite um número positivo:"))
num2 = float(input("Digite outro número positivo:"))

print()
print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número\n")
opcao = int(input("Escolha uma opção: "))

#Para otimizar o código, e não criar várias variáveis auxiliares, eu realizei a operação dentro dos print's utilizando f-string.
#Assim mantenho tudo em uma linha de código apenas.
if opcao == 1:
  print(f"A média ponderada entre {num1} e {num2} é: {(num1 * 2 + num2 * 3) / 5}")

elif opcao == 2:
  print(f"O quadrado da soma de {num1} e {num2} é:{(num1 + num2) ** 2}")

elif opcao == 3:
  print(f"O cubo do menor númeor é: {min(num1,num2) ** 3}")

else:
  print("Opção inválida. Informe uma opção válida para continuar.")