// Salário
#include <stdio.h>

int main() {

    float numero, horas, valorhora, salario;

    scanf("%f", &numero);
    scanf("%f", &horas);
    scanf("%f", &valorhora);

    salario = horas * valorhora;

    printf("NUMBER = %.0f\nSALARY = U$ %.2f\n", numero, salario);

    return 0;
}