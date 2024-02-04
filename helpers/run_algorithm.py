import time


def run_algorithm(algorithm, sortable):
    start = time.time()
    print("Tempo inicial: {}".format(start))

    algorithm(sortable)
    end = time.time()
    print("Tempo final: {}".format(end))
    print("O algoritmo levou {0:.2f} segundos para ser executado".format((end - start) % 60))

