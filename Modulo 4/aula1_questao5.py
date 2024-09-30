pessoas=int(input("Quantas pessoas: "))
i=0
idade=0
while pessoas > i:
    i+=1
    print('Participante:',i)
    idade+=int(input('Digite a idade do perticipante: '))
print('A media de idade dos participantes é',idade/pessoas)


