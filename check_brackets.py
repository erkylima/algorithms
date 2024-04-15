import math
import os
import random
import re
import sys
import copy


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here

    stack = []
    for i in s:
        if i == "[":
            stack.append("]")
        if i == "(":
            stack.append(")")
        if i == "{":
            stack.append("}")

        if i == ")" or i == "]" or i == "}":
            try:
                if i == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            except IndexError:
                stack.append(i)

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')