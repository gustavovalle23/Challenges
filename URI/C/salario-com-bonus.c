#include <stdio.h>

int main(){

    char nome;
    double salariofixo, vendas, salariofinal;

    scanf("%s", &nome);
    scanf("%lf", &salariofixo);
    scanf("%lf", &vendas);

    salariofinal = (vendas * 0.15) + salariofixo;

    printf("TOTAL = R$ %.2lf\n", salariofinal);

    return 0;
}