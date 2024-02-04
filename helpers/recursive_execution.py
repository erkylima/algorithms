from helpers.create_unordened_list import create_unordered_list
from helpers.run_recursive_algorithm import run_recursive_algorithm
from helpers.show_current_list import show_current_list


def recursive_execution(algorithm):
    sortable = create_unordered_list()

    show_current_list(sortable)  # perguntar se quer mostrar estado atual da lista

    sortable = run_recursive_algorithm(algorithm, sortable)

    show_current_list(sortable)  # perguntar se quer mostrar estado atual da lista
