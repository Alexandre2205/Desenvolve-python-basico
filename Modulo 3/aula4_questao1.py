# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
# Critério: se o resto da divisão do número por 2 for 0,
# o número é par, caso contrário é #ímpar. Lembre-se do operador do python % que
# retorna   o resto de uma divisão.
# entrada de dados
numero = int(input("Digite o primeiro numero: ")) + int(input("Digite o segundo numero: "))
print("O numero é par" if numero % 2 == 0 else "O numero é impar")
print("Fim")
