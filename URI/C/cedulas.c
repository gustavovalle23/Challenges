#include <stdio.h>

int main() {

int valor, cem, cinquenta, vinte, dez, cinco, dois, um;

//entrada do valor a ser calculado
scanf("%d", &valor);

cem = valor / 100;
cinquenta = (valor % 100) / 50;
vinte = ((valor % 100) - (cinquenta * 50)) / 20;
dez = (valor - ((cem * 100) + (cinquenta * 50) + (vinte * 20))) / 10;
cinco = (valor - ((cem*100) + (cinquenta*50) + (vinte*20) + (dez*10))) / 5;
dois = (valor - ((cem*100) + (cinquenta*50) + (vinte*20) + (dez*10) + (cinco*5))) / 2;
um = (valor - ((cem*100) + (cinquenta*50)+(vinte*20)+(dez*10)+(cinco*5)+(dois*2))) / 1;



printf("%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00\n",valor,cem,cinquenta,vinte, dez,cinco, dois,um);

return 0;
}
