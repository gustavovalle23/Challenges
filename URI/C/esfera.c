// Esfera
#include <stdio.h>
#include <math.h>

int main() {

    double raio, pi, volume;
    scanf("%lf", &raio);
    pi = 3.14159;
    volume = 4/3.0 * pi * pow(raio, 3);
    
    printf("VOLUME = %.3lf\n", volume);

return 0;
}