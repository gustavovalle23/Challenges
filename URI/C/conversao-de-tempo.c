// Conversão de Tempo
#include <stdio.h>

int main() {

int valor, hora, minuto, segundo;

scanf("%d", &valor);
// numa divisao entre numeros inteiros, o resultado sera a divisao inteira desses valores
    hora = valor / 3600;
        minuto = (valor - (hora*3600)) / 60  ;
            segundo = (valor - ((hora*3600) + (minuto*60)));

printf("%d:%d:%d\n", hora,minuto,segundo);
return 0;
}
