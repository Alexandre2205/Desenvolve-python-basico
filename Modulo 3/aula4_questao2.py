# Entrada de dados
nota=int(input('digite uma nota de 1 a 5 para o filme :'))
#Processamennto
if nota == 5:
    result='Excelente'
elif nota == 4:
    result='Muito bom'
elif nota == 3:
    result= 'Bom'
elif nota == 2:
    result= 'Regular'
elif nota == 1:
    result='Ruim'
#saida 
print('O filme avaliado é:',result)