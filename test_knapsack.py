from implementations.knapsackProblem import knapsack_dynamic_solution

if __name__ == '__main__':
    objects = {
        'weight': [0, 5, 6, 2, 7, 1],
        'value':  [0, 4, 1, 5, 7, 8]
    }
    max_weight = 7

    knapsack_dynamic_solution(objects, max_weight)