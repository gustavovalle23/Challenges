#include <stdio.h>
#include <stdlib.h>

int main(void){

    int dias, dia, mes, ano;
    scanf("%d", &dias);

    ano = dias / 365;
    mes = (dias - (ano * 365)) / 30;
    dia = dias - ((ano * 365) + (mes * 30));

    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", ano, mes, dia);

    return 0;
}