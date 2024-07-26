#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List


#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(array: List[int]) -> int:
    return sum(array)


if __name__ == '__main__':
    fptr = sys.stdout

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
