dias = int(input())

ano = dias // 365
mes = (dias - (ano * 365)) // 30
dia = dias - ((ano*365) + (mes * 30))

print("""{} ano(s)
{} mes(es)
{} dia(s)""".format(ano, mes, dia))
