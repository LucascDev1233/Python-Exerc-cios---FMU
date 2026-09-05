temp = float(input("Digite a temperatura da máquina: "))

print("-----------------------------------------------")

print(f"Temperatura: {temp}")
if temp < 40:
  print("Status: Normal")
elif temp >= 40 and temp <= 70: #posso também escrever elif temp <= 70
  print("Status: Atenção")
else:
  print("Status: Temperatura Crítica")
