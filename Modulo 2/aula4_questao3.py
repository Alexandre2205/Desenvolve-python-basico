# Dados do primeiro produto
nomep1= input('Digite o nome do produto 1: ')
unidadep1= float(input('Digite o preço unitário do produto 1: '))
quantidadep1= int(input('Digite a quantidade do produto 1: '))
# Dados do segundo produto
nomep2= input('Digite o nome do produto 2: ')
unidadep2= float(input('Digite o preço unitário do produto 2: '))
quantidadep2= int(input('Digite a quantidade do produto 2: '))
# Dados do terceiro produto
nomep3= input('Digite o nome do produto 3: ')
unidadep3= float(input('Digite o preço unitário do produto 3: '))
quantidadep3= int(input('Digite a quantidade do produto 3: '))
# Calculando
valor_total= unidadep1*quantidadep1+unidadep2*quantidadep2+unidadep3*quantidadep3
print(f"Total: R${valor_total:,.2f}")