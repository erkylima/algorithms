import time
from sorting_algorithms import insertion_sort, selection_sort, bubble_sort, quick_sort

import numpy as np


def main():
    while True:
        try:
            print("Escolha uma opção:")
            print("1. Bubble Sort")
            print("2. Selection Sort")
            print("3. Merge Sort")
            print("4. Quick Sort")
            print("5. Insertion Sort")
            print("6. Lista Encadeada")
            print("7. Pilha")
            print("8. Fila")
            print("9. Árvore Binária")
            print("0. Sair")

            choice = input("Digite o número da opção desejada: ")

            if choice == "0":
                print("Encerrando o programa. Até logo!")
                break
            elif choice == "1":
                run_algorithm(bubble_sort.BubbleSort)
            elif choice == "2":
                run_algorithm(selection_sort.SelectionSort)
            # elif choice == "3":
            #     merge_sort.run_example()
            # elif choice == "4":
            #     quick_sort.run_example()
            elif choice == "5":
                run_algorithm(insertion_sort.InsertionSort)
            # elif choice == "6":
            #     LinkedList.run_example()
            # elif choice == "7":
            #     Stack.run_example()
            # elif choice == "8":
            #     Queue.run_example()
            # elif choice == "9":
            #     BinaryTree.run_example()
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Você digitou algum valor inválido, tente novamente.")
        except:
            print("Algo deu errado, tente novamente.")
def run_algorithm(algorithm):
    # print("O algoritmo escolhido foi o {}".format(algorithm.__name__))
    amount: int = int(input("Digite o número de elementos que deseja: "))
    print("Foi criada uma lista de {} elementos\n================\nExecutando {}".format(amount, algorithm.__name__))
    start = time.time()
    sortable = list(np.random.random(amount))
    print("Tempo inicial: {}".format(start))
    algorithm(sortable)
    end = time.time()
    print("Tempo final: {}".format(end))
    print("O algoritmo levou {0:.2f} segundos para ser executado".format((end - start) % 60))
    show_list: str = input("Deseja mostrar a lista ordenada? (sim ou qualquer outra coisa é entendido com não): ")
    print(sortable) if show_list == "sim" else ""

if __name__ == "__main__":
    main()
