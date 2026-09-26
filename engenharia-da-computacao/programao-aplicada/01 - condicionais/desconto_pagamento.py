valorFinal = float(input("Digite o valor total da compra: "))
condicaoPagamento = int(input("Informe a condição de pagamento:"))

<<<<<<< HEAD
if formaPagamento == 1:
  percentual = 0.15

elif formaPagamento == 2:
  percentual = 0.10

elif formaPagamento == 3:
=======
if condicaoPagamento == 1:
  percentual = 0.15

elif condicaoPagamento == 2:
  percentual = 0.10

elif condicaoPagamento == 3:
>>>>>>> test
  percentual = 0.05

else:
  percentual = 0

if percentual > 0:
  print(f"O valor final a ser pago é: {valorFinal * (1 - percentual):.2f}")
else:
  print("Condição de pagamento inválida!")