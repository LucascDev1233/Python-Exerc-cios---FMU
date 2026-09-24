print("-------------SISTEMA DE SAQUE-------------")
login = input("Informe como quer ser chamado: ")
print(f"\nSeja Bem vindo {login} ao sistema de saque!\n")
senha = input("Cadastre a sua senha para continuar: ")
autenticacao = False


while not autenticacao:
  senha_correta = input("Digite sua senha:")
  if senha_correta != senha:
    print("Senha incorreta. Acesso negado.")
  elif senha_correta == senha:
    print("Senha correta! Acesso permitido")
    autenticacao = True

#Saldo e saque
print("\n----------SISTEMA DE SAQUE----------")


#Saldo, Saque e Depósito

saldo = 1000
executando = True

while executando:
  print(f"\nSaldo atual: R$ {saldo:.2f}")
  print("\nEscolha uma operação:")
  print("1 - Realizar Depósito")
  print("2 - Realizar Saque")
  print("3 - Sair do Sistema")
  opcao = int(input("\nDigite o número da operação desejada: "))

  if opcao == 1:
    valor_deposito = float(input("Digite o valor do depósito: R$ "))
    saldo += valor_deposito
    print(f"Depósito realizado com sucesso! Valor depositado R$ {valor_deposito:.2f}")

  elif opcao == 2:
    valor_saque = float(input("Digite o valor do saque: R$ "))
    if valor_saque > saldo:
      print("\nSaldo insuficiente para realizar o saque.")
    else:
      saldo -= valor_saque
      print(f"Saque realizado com sucesso! Valor sacado R$ {valor_saque:.2f}")
  elif opcao == 3:
    print(f"\nSaldo atual: R$ {saldo}")
    print("Obrigado por usar nosso sistema! Até logo!")
    executando = False
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
