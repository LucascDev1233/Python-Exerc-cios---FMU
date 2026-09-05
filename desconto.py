valor = float(input("Digite o valor da compra: "))

if valor < 100:
  percentual = 0
elif valor < 500:
  percentual = 10
else:
  percentual = 15

desconto = (valor * percentual) / 100
valor_final = valor - desconto

print(f"Valor da compra {valor:.2f}")
print(f"Desconto: {percentual:.1f}","%")
print(f"Valor descontado {desconto:.2f}")
print(f"Valor final: {valor_final:.2f}")