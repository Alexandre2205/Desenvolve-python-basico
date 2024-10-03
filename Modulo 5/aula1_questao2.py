import random
import math
soma=0
n=int(input('digite a quantidade de valores: '))
for i in range(n):
    soma+=random.randint(0,100)
print('A raiz quadrada é:',math.sqrt(soma))
