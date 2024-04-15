import time
from typing import List

from helpers.show_menu import show_menu
from sorting_algorithms import insertion_sort, selection_sort, bubble_sort, quick_sort
import types

import numpy as np


# def main():
#     show_menu()


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    product = [1] * n

    prefix = 1
    for i in range(n):
        product[i] *= prefix
        prefix *= nums[i]

    sufix = 1
    for i in range(n-1, -1, -1):
        product[i] *= sufix
        sufix *= nums[i]

    return product

def findMaxLength(nums: List[int]) -> int:
    count = 0
    maximo_atual = 0
    dic = {0: -1}
    atual = []
    for i, value in enumerate(nums):

        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in dic:
            maximo_atual = max(maximo_atual, i - dic[count])
        else:
            dic[count] = i
        atual.append(value)
        if count == 0 and len(atual) % 2 == 0:
            maximo_atual = len(atual)

    return maximo_atual

if __name__ == "__main__":
    print(findMaxLength([1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1]))
