def permutation(input_list):
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return [input_list]
    else:
        result = []
        for i in range(len(input_list)):
            element = input_list[i]
            other_elements = input_list[:i] + input_list[i + 1:]
            for p in permutation(other_elements):
                result.append([element] + p)
        return result


def permutation2(input_list):
    if len(input_list) == 0:
        yield []
    elif len(input_list) == 1:
        yield input_list
    else:
        for i in range(len(input_list)):
            element = input_list[i]
            other_elements = input_list[:i] + input_list[i + 1:]
            for p in permutation(other_elements):
                yeild[element] + p
