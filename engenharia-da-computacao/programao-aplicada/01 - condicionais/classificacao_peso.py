peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso / (altura ** 2)

print(f"\nSeu indice de massa corporal é: {imc:.2f}")

if imc < 18.5:
  print("Situação: Abaixo do peso")
elif imc < 25:
  print("Situação: Peso normal")
elif imc < 30:
  print("Situação: Sobrepeso")
elif imc < 35:
  print("Situação: Obesidade grau 1")
elif imc < 40:
  print("Situação: Obesidade grau 2")
else:
  print("Situação: Obesidade grau 3")