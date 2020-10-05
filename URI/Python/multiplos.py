# -*- coding: utf-8 -*-

def multiplos(a: str, b: str) -> str:
    a = float(a)
    b = float(b)

    if b % a == 0:
        return 'Sao Multiplos'
    elif a % b == 0:
        return 'Sao Multiplos'
    return 'Nao sao Multiplos'


if __name__ == "__main__":
    a, b = input().split()
    print(multiplos(a, b))
