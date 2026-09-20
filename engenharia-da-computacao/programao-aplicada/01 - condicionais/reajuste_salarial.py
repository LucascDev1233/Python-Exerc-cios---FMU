salario = float(input("Digite o seu salário atual: "))
cargo = input("Digite o seu cargo:")

#Defino para a condição apenas o valor do percentual, assim otimizando o código, podendo calcular apenas no final, referente a cada uma das profissões.
if cargo == "Programador de Sistemas":
  percentual = 0.3

elif cargo == "Analista de Sistemas":
  percentual = 0.2

elif cargo == "Analista de Banco de Dados":
  percentual = 0.15

else:
  print("Cargo inválido")

if percentual > 0:
  novo_salario = salario * (1 + percentual)
  print(f"Seu novo salário é: {novo_salario}")