estatura1 = float(input("Digite a primeira estatura: "))
estatura2 = float(input("Digite a segunda estatura: "))
estatura3 = float(input("Digite a terceira estatura: "))

if estatura1 == estatura2 or estatura1 == estatura3 or estatura2 == estatura3:
  print("Há, pelo menos, 2 pessoas com a mesma estatura.")
else:
  print(f"A maior estatura é: {max(estatura1, estatura2, estatura3)}")