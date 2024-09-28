classe= input('digite a classe do seu personagem(Mago, Guerreiro, Arqueiro): ')
forca= int(input('digite os pontos de força de seu personagem (1 a 20): '))
Magia= int(input('digite os pontos de magia de seu personagem (1 a 20): '))
# Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
# Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
# Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15
if classe == "Mago" or "mago":
    verifica= (forca < 10 and forca < 21) and (Magia >= 15 and Magia < 21)
elif classe == "Guerreiro" or "guerreiro":
    verifica= (forca >= 15 and forca < 21) and (Magia < 10 and Magia < 21)
elif classe == "Arqueiro" or "arqueiro":
    verifica= (forca > 5 and forca <= 15  and forca < 21) and (Magia > 5 and Magia <= 15 and Magia < 21)
# saida
print("Pontos de atributo consistentes com a classe escolhida: ",verifica)