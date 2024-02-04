import numpy as np


def create_unordered_list():
    amount: int = int(input("Digite o número de elementos que deseja: "))
    print("Foi criada uma lista de {} elementos\n================".format(amount))
    return list(np.random.rand(amount))