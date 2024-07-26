#!/bin/python3

import os


def aVeryBigSum(ar) -> int:
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    array = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(array)

    fptr.write(str(result) + '\n')

    fptr.close()
