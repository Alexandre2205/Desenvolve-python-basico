# Receber as medidas do terreno
comprimento= int(input('Digite o comprimento do lote: '))
largura= int(input('Digite a largura do lote: '))
# Recebendo o valor do metro quadrado
valor_metro= float(input('Digite o valor do metro quadrado: '))
# Calculando
Tamanho= comprimento*largura
valor= valor_metro*Tamanho
#mostrando o resultado
print(f"O terreno possui {Tamanho}m2 e custa R${valor:,.2f}")