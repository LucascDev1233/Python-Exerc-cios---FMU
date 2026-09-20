a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c
# Verifica se existem raízes reais
if delta > 0:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)

    print(f"As raízes são {raiz1} e {raiz2}")
#estava em dúvida se consideraria 0 como número real, por isso adicionei uma condição, para caso de ser 0 ele ainda realizar a conta

elif delta == 0:
    raiz = -b / (2 * a)

    print(f"A raiz é {raiz}")

else:
    print("Não existem raízes reais")