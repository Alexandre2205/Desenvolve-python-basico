n=int(input('Digite um numero: '))
maior=0
while n > 0:
    x=int(input('Digite outro numero: '))
    if x > maior:
        maior=x
    n=n-1
print("O maior valor digitado durante o laço foi",maior)