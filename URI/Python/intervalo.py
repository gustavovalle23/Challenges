def intervalo(num):
    if num >= 0 and num <= 25:
        return ('Intervalo [0, 25]')
    elif num > 25 and num <= 50:
        return ('Intervalo (25,50]')
    elif num > 50 and num <= 75:
        return ('Intervalo (50, 75]')
    elif num > 75 and num <= 100:
        return ('Intervalo (75, 100]')
    else:
        return ('Fora de intervalo')


if __name__ == '__main__':
    num = float(input())
    print(intervalo(num))