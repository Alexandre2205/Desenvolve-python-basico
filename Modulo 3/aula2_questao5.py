genero=input('Qual é o seu genero (F)feminino (M)masculino? ')
idade=int(input('Qual é sua idade? '))
trabalho=int(input("quantos anos você ja trabalhou? "))
#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.
aposenta= (genero == "F" and idade > 60) or (genero == "M" and idade > 65) or (trabalho > 30 or idade == 60 and trabalho >= 25)
print ("Beneficio de aposentadoria: ", aposenta)