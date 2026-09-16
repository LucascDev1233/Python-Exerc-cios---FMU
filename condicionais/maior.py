num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 == num2 and num1 == num3:
    exit()
if num1 > num2 and num1 > num3:
    print("O primeiro número é maior")
if num2 > num1 and num2 > num3:
    print("O segundo número é maior")
if num3 > num1 and num3 > num2:
    print("O terceiro número é maior")
