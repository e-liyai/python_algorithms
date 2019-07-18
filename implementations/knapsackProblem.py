def knapsack_dynamic_solution(objects, max_weight):
    # object should be in the form of:
    #       {
    #           'weight': [0, 5, 6, 2, 7, 1]
    #           'value':  [0, 4, 1, 5, 7, 8]
    #       }

    if not isinstance(objects, dict):
        return 'Object should be a dict'
    elif len(objects['weight']) != len(objects['value']):
        return 'weight value pair should be of same length'

    no_items = 0
    weight = 0
    two_dim_array = [[0 for i in range(max_weight + 1)] for x in range(len(objects['weight']))]

    while no_items <= len(objects['weight']):

        while weight <= max_weight:

            if no_items == 0 or weight == 0:
                two_dim_array[no_items][weight] = 0
            elif objects['weight'][no_items] <= weight:
                two_dim_array[no_items][weight] = max(
                    objects['value'][no_items] + two_dim_array[no_items - 1][weight - objects['weight'][no_items]],
                    two_dim_array[no_items - 1][weight]
                )
            else:
                two_dim_array[no_items][weight] = two_dim_array[no_items - 1][weight]

            weight += 1
        no_items += 1

    # print(two_dim_array[len(objects['weight'])][max_weight])
    print(two_dim_array)
