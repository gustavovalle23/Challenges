tempo = int(input())

hora = tempo // 3600
minuto = (tempo%3600) // 60
segundo = tempo - ((hora*3600) + (minuto*60))

print('{}:{}:{}'.format(hora, minuto, segundo))
