print("## Programa de empréstimo ##. \nResponda: sim ou não.")

nomeNegativado = input("Seu nome está negativado? (sim/não): ")

if nomeNegativado.lower() == "sim":
    print("Infelizmente, você não poderá realizar a compra.")

elif nomeNegativado.lower() == "não":
    carteira = input("Você trabalha com carteira assinada? (sim/não): ")

    if carteira.lower() == "sim":
        casa = input("Você possui casa própria? (sim/não): ")

        if casa.lower() == "sim":
            print("Você não poderá receber um empréstimo.")
        else:
            print("Você poderá receber um empréstimo!")

    else:
        print("Infelizmente, você não poderá realizar a compra.")

else:
    print("Resposta inválida. Digite 'sim' ou 'não'.")