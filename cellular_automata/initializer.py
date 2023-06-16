import numpy as np
import re
import random


def initial_configuration_setup(rows, cols):
    option = int(
        input(
            "Choose initial matrix configuration:\n1. N random points.\n2. N specific points.\n3. Random points specifying percentage of cells.\nOption: "
        )
    )
    return initialize_matrix(option, rows, cols)


def out_of_bounds(m, r, c):
    return 0 > r or r >= m.shape[0] or 0 > c or c >= m.shape[1]


def random_points_matrix(rows, cols, percentage):
    if percentage:
        p = float(input("Specify a percentage of the cells in ]0, 100]: "))
        n = int(p * (rows * cols) / 100)
    else:
        n = int(input("Specify how many points to start with: "))
    matrix = np.zeros((rows, cols), dtype="int32")
    coordinates = []
    for x in range(rows):
        for y in range(cols):
            coordinates.append((x, y))
    for i in range(n):
        index = random.randint(0, len(coordinates) - 1)
        x, y = coordinates.pop(index)
        matrix[x, y] = 1
    return matrix


def specific_points_matrix(rows, cols):
    while True:
        n = int(input("Specify how many points to start with: "))
        if n <= (rows * cols):
            break
        else:
            print("Number must be less than or equal to %d." % (rows * cols))
    matrix = np.zeros((rows, cols), dtype="int32")
    pattern = r"(\d+),(\d+)"
    print("Specify coordinates in the format x,y:")
    for i in range(n):
        while True:
            coordinate = input("Coordinate #%d: " % (i))
            match = re.search(pattern, coordinate)
            x = int(match.group(1))
            y = int(match.group(2))
            if not out_of_bounds(matrix, x, y) and matrix[x, y] == 0:
                matrix[x, y] = 1
                break
            else:
                print("Invalid coordinate or already chosen.")
    return matrix


def initialize_matrix(option, rows, cols):
    if option == 1:
        return random_points_matrix(rows, cols, False)
    elif option == 2:
        return specific_points_matrix(rows, cols)
    elif option == 3:
        return random_points_matrix(rows, cols, True)
    else:
        print("Not a valid option.")
        exit()
