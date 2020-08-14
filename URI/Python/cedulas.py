n1 = int(input())

cem = n1//100
cinquenta = (n1 - (cem*100)) // 50

vinte = (n1 - ((cem * 100) + (cinquenta * 50)) ) // 20

dez = (n1 - ((vinte*20) + (cem*100) + (cinquenta*50))    ) // 10

cinco = (n1 - ((dez*10) + (cem*100) + (cinquenta*50) + (vinte*20))  ) // 5

dois = (n1 - ((cem*100) + (cinquenta*50) + (vinte*20) + (dez*10) + (cinco*5)))            // 2

um = (n1 - ((cem*100) + (cinquenta*50) + (vinte*20) + (dez*10) + (cinco*5)+ (dois*2) ))     // 1

print('{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'.format(n1, cem, cinquenta, vinte, dez, cinco, dois, um))
