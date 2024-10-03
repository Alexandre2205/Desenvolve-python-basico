import random
n=random.randint(0,10)
while True:
    talvezn=int(input('Digite um numero: '))
    if talvezn==n:
        print('Correto! O numero é',n)
        break
    elif talvezn < n:
        print('Muito abaixo,tente novamente!')
        continue
    else:
        print('Muito alto, tente novamente!')
