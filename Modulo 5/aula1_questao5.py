import emoji
print('Emojis disponiveis: ')
print(emoji.emojize(":thumbs_up:"),'- :thumbs_up:')
print(emoji.emojize(":red_heart:"),' - :red_heart:')
print(emoji.emojize(":thinking_face:"),'- :thinking_face:')
print(emoji.emojize(":partying_face:"),'- :rpartying_face:')

frase=input('Digite uma frase e use algum emogi: ')
print(emoji.emojize(frase))

