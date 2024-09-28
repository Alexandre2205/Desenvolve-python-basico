#entrada de dados
peso=float(input('Digite o peso do produto a ser trasportado: '))
distancia=float(input('Digite a distancia em klm: '))
#processamento
if distancia <= 100:
    valor= peso*1
elif distancia > 100 and distancia < 300:
    valor= peso*1.50
elif distancia >= 300:
    valor= peso*2
if peso > 10:
    valor= valor+10
#saida
print('O frete custara R$',valor)