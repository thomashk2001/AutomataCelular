import sys
from initializer import initial_configuration_setup
from simulation import simulate_automaton
import neighbourhood as ng
import frontier as ft

def main():
    parameters = sys.argv[1:]
    if len(parameters) > 0:
        matrix_rows = int(parameters[0])
        matrix_cols = int(parameters[1])
        frontier_type = parameters[2]
        neighbourhood_type = parameters[3]
        neighbourhood_reach = parameters[4]
        iterations = int(parameters[5])

        matrix = initial_configuration_setup(matrix_rows, matrix_cols)
        frontier = ft.frontier(frontier_type)
        neighbourhood = ng.neighbourhood(neighbourhood_type, neighbourhood_reach, frontier)
        simulate_automaton(matrix, neighbourhood, iterations)

if __name__ == "__main__":
    main()
