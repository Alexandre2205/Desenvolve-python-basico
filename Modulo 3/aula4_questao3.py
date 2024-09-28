#Entrada de dados
ano=int(input('Digite o ano a ser consultado de é bissexto: '))
#Processamento
if ano%4==0 and (not ano%100 == 0) or ano%400 == 0:
    result='é'
else:
    result='não é'
#saida
print(f'O ano de {ano} {result} bissexto')