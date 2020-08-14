#include <stdio.h>

	void main() {

	double A, B, C, a, b, c, d, e;

	scanf("%lf", &A);
	scanf("%lf", &B);
	scanf("%lf", &C);

	a = A * C / 2;
	b = 3.14159 * C * C;
	c = (A+B) * C / 2;
	d = B * B;
	e = A * B;

	printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n", a, b, c, d, e);


}