a = float(input("N1:"))
op = input("op:")
b = float(input("N2:"))


if op == "+":
  print(a + b)
elif op == "-":
  print(a - b)
elif op == "*":
  print(a * b)
elif op == "/":
  if b == 0:
    print("Não é possível dividir por zero")
  else:
    print(a / b)