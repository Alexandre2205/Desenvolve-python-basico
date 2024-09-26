valor= int(input('Digite o valor a ser pago: '))
notas_100= int(valor/100)
valor=valor%100
notas_50=int(valor/50)
valor=valor%50
notas_20=int(valor/20)
valor=valor%20
notas_10=int(valor/10)
valor=valor%10
notas_5=int(valor/5)
valor=valor%5
notas_2= int(valor/2)
valor= valor%2
notas_1= int(valor/1)
print(notas_100,' nota(s) de R$100,00')
print(notas_50,' nota(s) de R$50,00')
print(notas_20,' nota(s) de R$20,00')
print(notas_10,' nota(s) de R$10,00')
print(notas_5,' nota(s) de R$5,00')
print(notas_2,' nota(s) de R$2,00')
print(notas_1,' nota(s) de R$1,00')