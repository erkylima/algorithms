from helpers.execution import execution
from helpers.recursive_execution import recursive_execution
from sorting_algorithms import bubble_sort, selection_sort, quick_sort, insertion_sort


def show_menu():
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
                execution(bubble_sort.bubble_sort)
            elif choice == "2":
                execution(selection_sort.selection_sort)
            # elif choice == "3":
            #     merge_sort.run_example()
            elif choice == "4":
                recursive_execution(quick_sort.quick_sort)
            elif choice == "5":
                execution(insertion_sort.insertion_sort)
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
