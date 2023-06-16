import numpy as np


def get_rules():
    bmin = int(input("Provide Bmin: "))
    bmax = int(input("Provide Bmax: "))
    dmin = int(input("Provide Dmin: "))
    dmax = int(input("Provide Dmax: "))
    return (bmin, bmax, dmin, dmax)


def print_matrix(matrix):
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if matrix[row, col]:
                print("■", end="")
            else:
                print("□", end="")
        print(end="\n")
    print(end="\n")


def simulate_automaton(matrix, neighbourhood, iterations):
    bmin, bmax, dmin, dmax = get_rules()
    future_matrix = np.copy(matrix)
    print_matrix(matrix)
    for i in range(iterations):
        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                on_neighbours = neighbourhood.count_neighbours(matrix, row, col)
                if (matrix[row, col] == 1 and bmin <= on_neighbours <= bmax) or (
                    matrix[row, col] == 0 and dmin <= on_neighbours <= dmax
                ):
                    future_matrix[row, col] = 1
                else:
                    future_matrix[row, col] = 0
        matrix = np.copy(future_matrix)
        print_matrix(matrix)
