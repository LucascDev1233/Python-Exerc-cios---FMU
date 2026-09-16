numeroCamisas = int(input("Digite o número de camisas que deseja comprar: "))
valorCamisa = 12.50
valorFinal = numeroCamisas * valorCamisa

if numeroCamisas <= 5:
    valorFinal = valorFinal * (1 - 3/100) # 3% de desconto, ao calcular o programa mostra que sobra 97 reais ou 97% do valor final, então multiplicamos o valor final por 0.97 ou 1 - 3/100.
else:
    if numeroCamisas <= 10: #aqui podiamos utilizar o elif, mas como o else já garante que o número de camisas é maior que 5, podemos apenas colocar um if dentro do else, que vai garantir que o número de camisas é maior que 5 e menor ou igual a 10
        valorFinal = valorFinal * (1 - 5/100)
    else:
        valorFinal = valorFinal * (1 - 7/100)

print(f"O valor total da compra será de R$ {valorFinal:.2f}.")

