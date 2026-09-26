valorFinal = float(input("Digite o valor total da compra: "))
formaPagamento = int(input("Informe a condição de pagamento:"))

if formaPagamento == 1:
  percentual = 0.20

elif formaPagamento == 2:
  percentual = 0.15

elif formaPagamento == 3:
  percentual = 0.10

else:
  percentual = 0

if percentual > 0:
  print(f"O valor final a ser pago é: {valorFinal * (1 - percentual):.2f}")
else:
  print("Condição de pagamento inválida!")