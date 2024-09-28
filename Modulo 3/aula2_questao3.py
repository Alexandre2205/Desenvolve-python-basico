#entrada de dados
idade=int(input('Digite sua idade: '))
jajogou3=input('Já jogou pelo menos 3 jogos de tabuleiro? (Sim ou Não) ')
jajogou3= 'sim' == jajogou3 or 'Sim' == jajogou3 or 'SIM' == jajogou3 or 'yes' == jajogou3 or 'True'
javenceu=int(input('Quantos jogos já venceu? '))
#processamento
apto= (idade >= 16 and idade <= 18) and (jajogou3 == True) and (javenceu >= 1)
#saida
print('Apto para ingressar no clube de jogos de tabuleiro: ',apto)