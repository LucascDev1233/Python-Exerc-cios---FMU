notas = [] #criei uma lista vazia

for i in range(1,5):
  nota = float(input(f'Digite uma nota {i}: ')) #pede que a pessoa escreva uma nota
  notas.append(nota) #armazena a nota digitada dentro da lista notas = []



media = sum(notas) / len(notas) # faz a soma dos números digitados e depois calcula a média.

print("\n----------------lANÇAMENTO DE NOTAS----------------")
print
print('Notas Digitados:', notas) #mostra todas as notas digitadas
print('A média do aluno foi:', media) # mostra o resultado da média



if media >= 5: # condição de que, se a media do aluno for maior ou igual a 5 então ele passa, se for menor que cinco então ele não passa.


  print('STATUS: O Aluno passou!')

else:

  print('STATUS: O Aluno reprovou!')

# adicionei duas variaveis, uma pra colocar a nota da recuperação e a outra pra juntar as duas notas, e tirar a média, sendo que o aluno tem que

#tirar mais que 5 para passar.

  recuperacao = float(input('\nDigite a nota da recuperção:'))
  mediageral= (recuperacao + media) / 2

  print('\nA media geral do aluno foi', mediageral)  # ele traz a media do aluno, com base na primeira média + a nota da recuperação.

  if mediageral <= 5:
   print('REPROVADO! BURRO!')

  else:
   print('PASSOU! Ufa, achei que não ia passar')