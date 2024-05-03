from problem import Problem
from uniform_cost_search import uniform_cost_search
# from a_star_misplaced import a_star_misplaced
# from a_star_euclidean import a_star_euclidean

def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(map(str, state[i:i+3])))

print("Welcome to JKR 8 puzzle solver.")
print("Type '1' to use a default puzzle, or '2' to enter your own puzzle:")
choice = int(input())

if choice == 1:
    initial_state = [1, 2, 3, 4, 8, 0, 7, 6, 5]
else:
    print("Enter your puzzle, use a zero to represent the blank")
    initial_state = []
    for i in range(3):
        row = input(f"Enter the {i+1} row, use space or tabs between numbers: ").split()
        initial_state.extend(map(int, row))

print("Enter your choice of algorithm:")
print("1. Uniform Cost Search")
print("2. A* with the Misplaced Tile heuristic")
print("3. A* with the Euclidean distance heuristic")
algorithm_choice = int(input())

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
problem = Problem(initial_state, goal_state)

if algorithm_choice == 1:
    solution_node = uniform_cost_search(problem)
# elif algorithm_choice == 2:
#     solution_node = a_star_misplaced(problem)
# elif algorithm_choice == 3:
#     solution_node = a_star_euclidean(problem)
else:
    print("Invalid choice of algorithm.")
    exit()

if solution_node:
    solution_path = solution_node.path()
    print("Expanding state:")
    print_state(initial_state)
    print("The best state to expand with g(n) = {} and h(n) = {} is...".format(solution_path[-1].cost, solution_node.cost - solution_path[-1].cost))
    print_state(solution_path[-1].state)
    print("Expanding this node...")
    for i in range(1, len(solution_path)):
        print("The best state to expand with g(n) = {} and h(n) = {} is...".format(solution_path[i].cost, solution_node.cost - solution_path[i].cost))
        print_state(solution_path[i].state)
        print("Expanding this node...")
    print("Goal!!!")
else:
    print("No solution found.")
