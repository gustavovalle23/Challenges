#!/bin/python3

import sys
from typing import List


def compareTriplets(a: List[int], b: List[int]) -> List[int]:
    alice_points = 0
    bob_points = 0

    if a[0] > b[0]:
        alice_points += 1
    elif a[0] < b[0]:
        bob_points += 1

    if a[1] > b[1]:
        alice_points += 1
    elif a[1] < b[1]:
        bob_points += 1

    if a[2] > b[2]:
        alice_points += 1
    elif a[2] < b[2]:
        bob_points += 1

    return [alice_points, bob_points]


if __name__ == '__main__':
    fptr = sys.stdout

    array_a = list(map(int, input().rstrip().split()))

    array_b = list(map(int, input().rstrip().split()))

    result = compareTriplets(array_a, array_b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
