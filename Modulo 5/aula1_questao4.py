from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
e_hora_atuais = datetime.now()
e_hora_em_texto = e_hora_atuais.strftime('%H:%M')

print("Data:",data_e_hora_em_texto)
print("Hora:",e_hora_em_texto)