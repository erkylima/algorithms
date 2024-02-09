from helpers.create_unordened_list import create_unordered_list
from helpers.run_algorithm import run_algorithm
from helpers.show_current_list import show_current_list


def execution(algorithm):
    sortable = create_unordered_list()
    sortable.sort()
    show_current_list(sortable)  # perguntar se quer mostrar estado atual da lista

    run_algorithm(algorithm, sortable)

    show_current_list(sortable)  # perguntar se quer mostrar estado atual da lista


