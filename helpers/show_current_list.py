def show_current_list(current):
    show_list: str = input("Deseja mostrar a lista desordenada? (sim ou qualquer outra coisa é entendido com não): ")
    print(current) if show_list == "sim" else None
