# -*- coding: utf-8 -*-

dia_in = int(input().split()[1])
hours = input().split()
hours.remove(':')
hours.remove(':')
hora_in, min_in, sec_in = hours

hora_in = int(hora_in)
min_in = int(min_in)
sec_in = int(sec_in)


dia_fim = int(input().split()[1])
hours = input().split()
hours.remove(':')
hours.remove(':')
hora_fim, min_fim, sec_fim = hours

hora_fim = int(hora_fim)
min_fim = int(min_fim)
sec_fim = int(sec_fim)


minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
inicio = sec_in + min_in*minuto_seg + hora_in*hora_seg + dia_in*dia_seg
fim = sec_fim + min_fim*minuto_seg + hora_fim*hora_seg + dia_fim*dia_seg

tempo = fim - inicio
dias = int(tempo/dia_seg)
tempo = tempo%dia_seg
horas = int(tempo/hora_seg)
tempo = tempo%hora_seg
minutos = int(tempo/minuto_seg)
tempo = tempo%minuto_seg
segundos = tempo
print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')