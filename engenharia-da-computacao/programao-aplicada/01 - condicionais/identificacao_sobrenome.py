sobrenome = input("Digite o sobrenome do apresentador: \n").upper() #adicionei .upper() para que mesmo que o usuário digite o sobrenome em letras minúsculas, o programa possa reconhecer.
if sobrenome == "PINHEIRO" or sobrenome == "ARAÚJO":
  print("O telejornal apresentado é: Bom dia Nação")
elif sobrenome == "BONNER" or sobrenome == "VASCONCELOS":
  print("O telejornal apresentado é: Jornal Brasileiro")
else:
  print("Apresentador(a) desconhecido(a).")