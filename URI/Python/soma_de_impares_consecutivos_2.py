times = int(input())

somas = []
for _ in range(times):
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    n1, n2 = numbers
    soma = 0
    for n in range(n1+1, n2):
        if n % 2 == 1:
            soma += n
    somas.append(soma)

[print(x) for x in somas]
