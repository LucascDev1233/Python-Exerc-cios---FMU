print("****TABELA VERDADE****\n")
print("1. Operador AND")
print("2. Operador OR")
print("3. Operador NOT\n")

opcao = int(input("Escolha uma opção: (1, 2 ou 3) "))

if opcao in [1,2]:
  bit1 = bool(int(input("Informe um bit (0 ou 1): ")))
  bit2 = bool(int(input("Informe o segundo bit (0 ou 1): ")))

  if opcao == 1:
    print(f"O resultado da operação AND entre {bit1} e {bit2} é: {bit1 and bit2}\n")
  else:
    print(f"O resultado da operação OR entre {bit1} e {bit2} é: {bit1 or bit2}\n")

elif opcao == 3:
    bit = bool(int(input("Informe um bit (0 ou 1): ")))
    print(f"O resultado da operação {opcao} entre {bit} é: {not bit}\n")

else:
  print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")



