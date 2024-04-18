#!/bin/python3
import copy
import math
import os
import random
import re
import sys
import random


#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here

    last = copy.copy(a[:1])
    result = []
    for i, value in enumerate(a):
        if i > 0:
            last.append(value)
        last[0:i + 1] = sorted(last[0:i + 1])
        if i == 0:
            last[i] = float(value)
            result.append(last[i])
            continue
        if i == 1:
            last[i] = float((last[i] + last[i - 1]) / 2)
            result.append(last[i])
            continue
        if i % 2 != 0:
            half = (i // 2)
            median = float((last[half] + last[half + 1]) / 2)
            result.append(median)
        if i % 2 == 0:
            half = (i // 2)
            result.append(value)

    return result

if __name__ == '__main__':

    a_c = 10
    a = []
    for _ in range(a_c):
        # a = random.sample(range(10, 30), 5)
        a.append(int(input()))
    print(a)


    result = runningMedian(a)
    print(result)
