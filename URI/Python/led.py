# -*- coding: utf-8 -*-

def led():
    n = int(input())

    n_leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, 
            '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}


    numbers = []
    numbers_split = []
    leds = []

    for i in range(n):
        numbers.append(input())
        numbers_split.append(list(numbers[i]))


    for i in range(n):
        for j in range(len(numbers_split[i])):
            leds.append(n_leds[numbers_split[i][j]])
        print(f'{sum(leds)} leds')
        leds.clear()


if __name__ == "__main__":
    led()