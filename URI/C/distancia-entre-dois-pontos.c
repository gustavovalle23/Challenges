// Distância Entre Dois Pontos

#include <stdio.h>
#include <math.h>

int main(){

    float x1, y1, x2, y2, potencia1, potencia2, distancia;
    scanf("%f %f %f %f", &x1, &y1, &x2, &y2);

    potencia1 = x2 - x1;
    potencia2 = y2 - y1;
    distancia = sqrt((potencia1 * potencia1) + (potencia2 * potencia2));

    printf("%.4f\n", distancia);

    return 0;
}
