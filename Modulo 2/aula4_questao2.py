# RECEBENDO A TEMPERATURA EM GRAUS FAHRENHEIT
tempF= float(input('Digite a temperatura em graus Fahrenheit: '))
# CONVERTENDO EM GRAUS CELSIUS
tempC= (tempF-32)*(5/9)
# MOSTRANDO RESULTADO
print(f"{tempF:.0f} graus Fahrenheit são {tempC:.0f} graus Celsius.")
