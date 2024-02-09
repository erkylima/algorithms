from data_structure.stack.node import Node


class Stack(object):
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)  # Cria novo nó
        if self._top:  # Verifica se topo da pilha não é nulo
            new_node.next = self._top  # adiciona o ponteiro do topo para próximo nó
        self._top = new_node  # nó do topo é o que acaba de ser criado
        self._size += 1

    def push_string_stack(self, value):
        if isinstance(value, str):
            for e in value:
                self.push(e)
        else:
            raise TypeError('Not a string')

    def pop(self):
        temp_node = self._top
        self._top = self._top.next
        self._size -= 1
        return temp_node

    def peek(self):
        return self._top.value

    def __len__(self) -> int:
        return self._size

    def is_empty(self):
        return self._size == 0

    def reverse(self):
        reversed_stack = Stack()
        while not self.is_empty():
            top = self.pop()
            reversed_stack.push(top.value)
        self._top = reversed_stack.pop()

    def __str__(self):
        temp = self._top
        temp_list = []
        while temp:
            temp_list.append(str(temp.value))
            temp = temp.next
        return str(temp_list)

    def __menu__(self):
        while True:
            try:
                print("O que deseja fazer:")
                print("1. Inserir valor")
                print("2. inserir palavra completa")
                print("3. Buscar e remover ultimo item")
                print("4. reverter ordem da pilha")
                print("5. Tamanho da Pilha")
                print("6. Imprimir Pilha")
                print("7. Verificar se pilha está vazia")
                print("0. Voltar")

                choice = input("Digite o número da opção desejada: ")

                if choice == "0":
                    print("Encerrando o programa. Até logo!")
                    break
                elif choice == "1":
                    value = input("Digite o valor: ")
                    self.push(value)
                elif choice == "2":
                    value = input("Digite o valor: ")
                    self.push(value)
                elif choice == "3":
                    value = self.pop()
                    print("Valor removido da pilha: {}".format(value))
                elif choice == "4":
                    self.reverse()
                    print("Pilha revertida com sucesso")
                elif choice == "5":
                    print("O tamanho da pilha é {} elementos".format(self.__len__()))
                elif choice == "6":
                    print("Imprimindo Pilha: \n {}".format(self.__str__()))
                elif choice == "7":
                    isornot = ""
                    if self.is_empty():
                        isornot = "sim"
                    else:
                        isornot = "não"

                    print("Pinha está vazia? {}".format(isornot))
            except TypeError:
                print("Você precisa digitar um texto")
            except:
                print("Algum erro ocorreu")
