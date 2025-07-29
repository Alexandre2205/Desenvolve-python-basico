#Recebe valor de quntos experimentos precisa
experimento = int(input('Digite a quantidade de experimentos: '))

#Declarando as variaveis 
rato, coelho, sapo = 0 ,0 ,0

while experimento > 0 :
  #Variavel de iteração
  experimento = experimento - 1

  #Coleta quantidade de animais
  quantidade = int(input('Digite a quntidade de animais neste experimento: '))

  #Coleta qual animal esta sendo usuado pela primeira letra
  animal = (input('Digite a primeira letra da espécie do animal utilizado: '))

  # Cadeia de if armazena a quantidade de cada animal de acordo com a primeira letra
  if animal == 'S' or animal == 's':
    sapo += quantidade
  elif animal == 'C' or animal == 'c':
    coelho += quantidade
  elif animal == 'R' or animal == 'r':
    rato += quantidade
  else:
# Caso a pessoa digite a inicial errada a variavel de iteração recebe +1 e volta a repetir a quantidade certa
    experimento = experimento + 1
    print('Você escolheu um animal invalido, tente novamente.')
total = sapo+coelho+rato
print("Quantidade total de animais: ",total )
#total de cada especie
print("Quantidade total de rato: ",rato )
print("Quantidade total de coelho: ",coelho )
print("Quantidade total de sapo: ", sapo )
#percentual
print(f"Percentual de ratos: {(rato/total*100):.2f}%")
print(f"Percentual de coelhos: {(coelho/total*100):.2f}%")
print(f"Percentual de sapos: {(sapo/total*100):.2f}%")

