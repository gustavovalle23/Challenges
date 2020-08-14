// Cálculo Simples
#include <stdio.h>

int main() {
    
    int peca1, peca2, numero1, numero2;
    float valor1, valor2, total;

    scanf("%d%d%f", &peca1, &numero1, &valor1);
    scanf("%d%d%f", &peca2, &numero2, &valor2);

    total = (numero1*valor1) + (numero2*valor2);    

    printf("VALOR A PAGAR: R$ %.2f\n", total);

return 0;