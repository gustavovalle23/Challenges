// Gasto de Combustível
#include <stdio.h>

int main() {

float t, v, distancia, litros;
scanf("%f%f", &t, &v);

distancia = t * v;
litros = distancia / 12;

printf("%.3f\n", litros);


return 0;
}
