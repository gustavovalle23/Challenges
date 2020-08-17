# -*- coding: utf-8 -*-

if __name__ == '__main__':
    def formula_bhaskara(a: float, b: float, c: float):
        try:
            delta = b**2 - (4*a*c)
            root_delta = delta**(1/2)
            x1 = (b*(-1) + root_delta) / (2*a)
            x2 = (b*(-1) - root_delta) / (2*a)
            print('R1 = %.5f' % x1)
            print('R2 = %.5f' % x2)
        except:
            return print('Impossivel calcular')

    values: list = input().split(' ')
    a: float = float(values[0])
    b: float = float(values[1])
    c: float = float(values[2])

    formula_bhaskara(a, b, c)
